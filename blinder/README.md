# F.A.Q 

# LICENSE
EULA

- logo
<div align="center">
    <img src="http://oi66.tinypic.com/2j0lgub.jpg" width="600px"</img> 
</div>

- interface
<div align="center">
    <img src="http://oi65.tinypic.com/6yzdk7.jpg" width="600px"</img> 
</div>


# What is blinder?
- It can perform a blind mitm attack by redirecting victim traffic into our localhost
- It will not alert IDS/Firewalls and no noise
- It will use datagram redirection code in network/transport layer to communicate with TCP-IP

# Advantage
- Sniff traffic using your localhost

# Attack Technique
- This use ICMP TYPE 5 Attack, using IP Datagram of Transport Protocol used in Transport Layer 4 in OSI Model

# Blind Attacks
- Blind  : ICMPAttack.py -v -i wlan0 -g 192.168.15.0 -t 192.168.15.18 && bettercap -t 127.0.0.1 --proxy -P POST
- Blind  : ICMPAttack.py -v -i wlan0 -g 192.168.15.0 -t 192.168.15.18 && sslstrip -a -k -l 8080 -i logs.txt

# Tips
- Try to lock victim accounts, 90% of the time, victim will use gmail to recover password

# Breaking HTTPS
- See traffic using localhost for PC, Mobile, I-PAD, Tablets

# Installation
- Perl script to form automated and guided attack
- Manual python script to redirect traffic and integrate it with other tools as well

# Requirements
- In terminal: sudo apt-get install bettercap
- In terminal: Perl -MCPAN -e shell, then, install Term::ANSIColor

# Contact
- mrharoonawan@gmail.com
