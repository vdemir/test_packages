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
			 GIO_LIBS='-L/usr/lib -lgio-2.0 -lgobject-2.0 -lglib-2.0'  \
                         GIO_CFLAGS='-I/usr/include/glib-2.0/ -I/usr/lib/glib-2.0/include -I/usr/include/gio-unix-2.0' \
			 DBUS_LIBS=-L/usr/lib \
		         DBUS_CFLAGS=-I/usr/include/dbus-1.0 \
                         MENU_CACHE_LIBS=-L/usr/lib \
			 MENU_CACHE_CFLAGS=-I/usr/include/menu-cache/ ")
                         

def build():
     autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())