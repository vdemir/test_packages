#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get


 
def setup():
    
    autotools.configure("--prefix=/usr -enable-shared --disable-static \
                         --without-gtk  --disable-gtk-doc \
                         --enable-udisks --enable-actions --sysconfdir=/etc")

#                        --without-gtk  --disable-gtk-doc \	                                  
def build():
     autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())