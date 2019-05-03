#***************************************************************************************#
#----------------------- EULA LICENSE AGREEMENT NOTICE ---------------------------------#
#1. This software uses EULA based software agreement that grants users rights to use for#
#any purpose, modify and redistribute creative works about this perl software.          #
#2. This software comes in "is-as" warranty, author "Haroon Awan" take no responsbility #
#what you do with by/this software. Your free to use this software as it is for any     #
#purpose that suites as long as it is not related to crime.                             #
#***************************************************************************************#

#!/bin/bash
sed 's~http[s]*://~~g' bingsubdomain.txt
sed 's/\.com.*/.com/' bingsubdomain.txt > bingsubdomains
sed 's~http[s]*://~~g' bingsubdomains > bingsubdomain.txt
./bingchecker.sh