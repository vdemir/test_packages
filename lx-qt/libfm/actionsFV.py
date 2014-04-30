#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
 
def setup():
 
 
    autotools.configure("--prefix=/usr -enable-shared --without-gtk --disable-static --disable-gtk-doc \
                         --enable-udisks --enable-actions --sysconfdir=/etc \
                         GIO_LIBS=-L/usr/lib GIO_CFLAGS=I-/usr/include \
                         DBUS_LIBS=-L/usr/lib DBUS_CFLAGS=I-/usr/include \
                         MENU_CACHE_CFLAGS=I-/usr/include MENU_CACHE_LIBS=L-/usr/lib ")
                         #GTK_CFLAGS=I-/usr/lib GTK_LIBS=L-/usr/include CPPFLAGS=-I/usr/bin LDFLAGS=-L/usr/bin \
    
def build():
    #autotools.make('CFLAGS="%s `pkg-config glib-2.0 --cflags`"' % get.CFLAGS())
    cmaketools.make('CC="%s" CFLAGS="%s" CXFLAGS="%s"' % (get.CC(), get.CFLAGS(),get.CXFLAGS()))
 

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())