#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def install():
	
    pisitools.dobin("runanki", "/usr/bin/")
    pisitools.insinto("/usr/share/", "anki")
    pisitools.insinto("/usr/share/", "aqt")
    #pisitools.domove("anki", "/usr/share/")
    #pisitools.domove("aqt", "/usr/share/")
