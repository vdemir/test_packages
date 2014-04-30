#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools

def setup():
    shelltools.export("LDFLAGS", "%s -lgio-2.0 -lgobject-2.0 -Wl,--export-dynamic -lgmodule-2.0 -pthread -lglib-2.0"  % get.LDFLAGS())
   
    if get.buildTYPE() == "emul32":
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())
        shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

    libtools.libtoolize("--copy --force")
    autotools.autoreconf("-vif")
    autotools.configure()

def build():
    autotools.make()

def check():
    autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
