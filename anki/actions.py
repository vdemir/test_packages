#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
def install():
    #shelltools.makedirs("%s/usr/share/man/man1/" % get.installDIR())
    pisitools.dodoc("anki.1")
    shelltools.makedirs("%s/usr/local/bin/anki" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
#    

#    pisitools.dobin("anki")


# By PiSiDo 2.0.0
