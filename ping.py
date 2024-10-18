from scapy.all import *

ping = ICMP(type=8)

packet = IP(src="10.33.73.77", dst="10.33.73.72")

frame = Ether(src="98:8D:46:C4:FA:E5", dst="30:89:4a:d2:5a")

final_frame = frame/packet/ping

answers, unanswered_packets = srp(final_frame, timeout=10)

print(f"Pong reçu : {answers[0]}")
