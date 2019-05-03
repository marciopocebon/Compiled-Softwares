#!/bin/bash
chmod u+x *.sh
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/perl:~/root/Downloads/ShaheenX/
alias myscript=~/root/Downloads/ShaheenX/
cd /usr/bin
ln -fsT /root/Downloads/ShaheenX/ShaheenX.pl /usr/bin/ShaheenX
chmod u+x ShaheenX.pl
chmod u+x *.sh
chmod u+x /usr/bin/ShaheenX
echo "Installed!"
echo "ShaheenX can be called anywhere from system"
