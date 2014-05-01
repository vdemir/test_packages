#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/lxqt-globalkeys/work/ and:
# WorkDir="lxqt-globalkeys-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=release -DCMAKE_INSTALL_PREFIX=/usr")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("lxqt-globalkeys")

# You can use these as variables, they will replace GUI values before build.
# Package Name : lxqt-globalkeys
# Version : 1.0
# Summary : Daemon used to register global keyboard shortcuts

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
