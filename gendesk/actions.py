#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools

# if pisi can't find source directory, see /var/pisi/gendesk/work/ and:
# WorkDir="gendesk-"+ get.srcVERSION() +"/sub_project_dir/"

def build():

shelltools.cd("%s/" % get.workDIR())  
shelltools.system("go build")

#def install():
#    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

# By PiSiDo 2.0.0
