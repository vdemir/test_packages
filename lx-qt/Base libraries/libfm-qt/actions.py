#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt


from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools

def setup():
    shelltools.system("./autogen.sh --enable-shared --disable-static \
				    --enable-udisks --disable-actions \
                                    --disable-demo --disable-dependency-tracking \
                                    --prefix=/usr --libdir=/usr/lib --enable-fast-install=autogen")
#--without-gtk \--disable-gtk-doc
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "COPYING")