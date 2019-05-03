#***************************************************************************************#
#----------------------- EULA LICENSE AGREEMENT NOTICE ---------------------------------#
#1. This software uses EULA based software agreement that grants users rights to use for#
#any purpose, modify and redistribute creative works about this perl software.          #
#2. This software comes in "is-as" warranty, author "Haroon Awan" take no responsbility #
#what you do with by/this software. Your free to use this software as it is for any     #
#purpose that suites as long as it is not related to crime.                             #
#***************************************************************************************#


#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/perl:/usr/sbin/python:/usr/bin/python:~/root/Downloads/vasl-master/
alias myscript=~/root/Downloads/vasl-master/
cd /usr/bin
ln -fsT /root/Downloads/vasl-master/vasl.py /usr/bin/vasl
chmod u+x /root/Downloads/vasl-master/vasl.py
chmod u+x /root/Downloads/vasl-master/cleaner.sh
chmod u+x /usr/bin/vasl
cd /root/
echo "Installed!"
echo "VASL can be called anywhere from system"
