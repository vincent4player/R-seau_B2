TP4 SECU : Exfiltration


I. Getting started Scapy
➜ Déjà, allez manger le cours sur Scapy et testez vous-même tous les exemples donnés là-bas
🌞 ping.py

```
PS D:\Reseau-Linux\R-seau_B2> python .\ping.py
>>
Begin emission

Finished sending 1 packets
.*
Received 2 packets, got 1 answers, remaining 0 packets
Pong reçu : QueryAnswer(query=<Ether  dst=f2:39:c5:c0:07:e5 src=98:8D:46:C4:FA:E5 type=IPv4 |<IP  frag=0 proto=icmp src=10.33.73.77 dst=10.33.67.174 |<ICMP  type=echo-request |>>>, answer=<Ether  dst=98:8d:46:c4:fa:e5 src=f2:39:c5:c0:07:e5 type=IPv4 |<IP  version=4 ihl=5 tos=0x0 len=28 id=13993 flags= frag=0 ttl=64 proto=icmp chksum=0xa2fb src=10.33.67.174 dst=10.33.73.77 |<ICMP  type=echo-reply code=0 chksum=0xffff id=0x0 seq=0x0 unused=b'' |<Padding  load=b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' |>>>>)
PS D:\Reseau-Linux\R-seau_B2>
```

🌞 tcp_cap.py

```
PS D:\Reseau-Linux\R-seau_B2> python .\tcp_cap.py
TCP SYN ACK reçu !
- Adresse IP src : 140.82.112.26
- Adresse IP dest : 10.33.73.77
- Port TCP src : 443
- Port TCP dst : 50414
PS D:\Reseau-Linux\R-seau_B2>
```

🌞 dns_cap.py

```
PS D:\Reseau-Linux\R-seau_B2> python .\tcp_cap.py dns_cap.py 
Begin emission:
Finished sending 1 packets.
...*
Received 4 packets, got 1 answers, remaining 0 packets
104.26.10.233
```

🌞 dns_lookup.py

```
PS D:\Reseau-Linux\R-seau_B2> python .\dns_lookup.py
DNS Ans 172.67.74.226
PS D:\Reseau-Linux\R-seau_B2>
```

🌞 arp_poisoning.py


🌞 icmp_exf_send.py

```
PS D:\Reseau-Linux\R-seau_B2> python .\icmp_exf_send.py  10.33.73.72 j
.
Sent 1 packets.
```
```
voir wireshark
```

🌞 icmp_exf_receive.py

```
PS D:\Reseau-Linux\R-seau_B2> python .\icmp_exf_receive.py  10.33.73.72 yoyo
.
Sent 1 packets.
```