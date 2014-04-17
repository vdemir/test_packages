#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools

def build():

    shelltools.cd("%s/gendesk-"+ get.srcVERSION()/" % get.workDIR())  
    shelltools.system("go build")

def install():
    shelltools.move("%s/gendesk-"+ get.srcVERSION()/gendesk-"+ get.srcVERSION()", "%s/usr/bin/" % get.workDIR(),get.installDIR())
    