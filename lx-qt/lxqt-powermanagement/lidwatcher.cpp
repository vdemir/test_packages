/* BEGIN_COMMON_COPYRIGHT_HEADER
 * (c)LGPL2+
 *
 * LXDE-Qt - a lightweight, Qt based, desktop toolset
 * http://razor-qt.org
 *
 * Copyright: 2012 Razor team
 * Authors:
 *   Christian Surlykke <christian@surlykke.dk>
 *
 * This program or library is free software; you can redistribute it
 * and/or modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.

 * You should have received a copy of the GNU Lesser General
 * Public License along with this library; if not, write to the
 * Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
 * Boston, MA 02110-1301 USA
 *
 * END_COMMON_COPYRIGHT_HEADER */
#include <QTimer>
#include <QCoreApplication>
#include <lxqt/lxqtautostartentry.h>
#include <QtCore/qprocess.h>
#include <QtCore/qtextstream.h>
#include <QDebug>
#include "lidwatcher.h"
#include "../config/powermanagementsettings.h"

LidWatcher::LidWatcher(QObject *parent) : Watcher(parent)
{
    qDebug() << "Starting lidwatcher";
    connect(&mLid, SIGNAL(changed(bool)), this, SLOT(lidChanged(bool)));
}

LidWatcher::~LidWatcher(){
    qDebug() << "Stopping lidwatcher";
}

void LidWatcher::lidChanged(bool closed)
{
    qDebug() << "LidWatcherd#lidChanged: closed=" << closed;
    if (closed)
    {
        doAction(action());
    }
}

int LidWatcher::action()
{
    if (mSettings.isEnableExtMonLidClosedActions() && externalMonitorPlugged())
    {
        if (mLid.onBattery())
        {
            return mSettings.getLidClosedExtMonAction();
        }
        else
        {
            return mSettings.getLidClosedExtMonAcAction();
        }
    }
    else
    {
        if (mLid.onBattery())
        {
            return mSettings.getLidClosedAction();
        }
        else
        {
            return mSettings.getLidClosedAcAction(); 
        }
    }
}

bool LidWatcher::externalMonitorPlugged()
{
    int monitorCount = 0;

    QProcess xrandr(this);
    xrandr.start("xrandr", QIODevice::ReadOnly);
    xrandr.waitForFinished(1000);

    if (xrandr.exitCode() != 0)
    {
        return false; // Well, what to do?
    }

    QTextStream xrandr_stdout(&xrandr);
    while (!xrandr_stdout.atEnd())
    {
        QString line = xrandr_stdout.readLine();
        qDebug() << ">>" << line;
        if (line.indexOf(" connected", 0) > -1)
        {
            monitorCount++;
        }
    }

    qDebug() << "monitorCount: " << monitorCount;

    return monitorCount >= 2;
}
