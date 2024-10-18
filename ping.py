from scapy.all import *

ping = ICMP(type=8)

packet = IP(src="10.33.73.77", dst="10.33.67.174")

frame = Ether(src="98:8D:46:C4:FA:E5", dst="f2:39:c5:c0:07:e5")

final_frame = frame/packet/ping

answers, unanswered_packets = srp(final_frame, timeout=10)

print(f"Pong reçu : {answers[0]}")
