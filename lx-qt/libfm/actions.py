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
    
    autotools.configure("--prefix=/usr -enable-shared --disable-static --without-gtk  --disable-gtk-doc \
                         --enable-udisks --enable-actions --disable-demo --sysconfdir=/etc \
			 GIO_LIBS='-L/usr/lib -lgio-2.0 -lgobject-2.0 -lglib-2.0 -ldbusmenu-qt -ldbusmenu-glib' \
                         GIO_CFLAGS='-I/usr/include/glib-2.0/ -I/usr/include/gio-unix-2.0 -I/usr/lib/glib-2.0/include' \
			 DBUS_LIBS='-L/usr/lib -ldbusmenu-glib -ldbusmenu-qt -ldbus-c++-1 -ldbus-glib-1 -ldbus-1' \
		         DBUS_CFLAGS='-I/usr/include/dbus-1.0 -I/usr/include/libdbusmenu-glib-0.4 -I/usr/include/dbusmenu-qt' \
                         MENU_CACHE_LIBS='-L/usr/lib -lmenu-cache' \
			 MENU_CACHE_CFLAGS=-I/usr/include/menu-cache/ ")
 	                                  
def build():
     autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())