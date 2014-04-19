#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/jedit/work/ and:
# WorkDir="jedit-"+ get.srcVERSION() +"/sub_project_dir/"


 #def build():
  #  shelltools.system("unzip -o jedit5.2pre1install.jar")
   # shelltools.system("tar jxf installer/jedit-api.tar.bz2")

def install():
    shelltools.system("java -jar jedit5.2pre1install.jar auto %s/usr/share/java/jedit unix-script=%s/usr/bin unix-man=%s/usr/share/doc" % (get.installDIR(), get.installDIR(), get.installDIR()))



# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("jedit")

# You can use these as variables, they will replace GUI values before build.
# Package Name : jedit
# Version : 5.1.0
# Summary : Programmers test editor

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
