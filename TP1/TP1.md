TP1 : Maîtrise réseau du votre poste

I. Basics

☀️ Carte réseau WiFi
Déterminer...
```
Adresse physique . . . . . . . . . . . : 98-8D-46-C4-FA-E5
Adresse IPv4. . . . . . . . . . . . . .: 10.33.73.77(préféré)

CIDR:  Masque de sous-réseau. . . . . . . . . : 255.255.240.0☀️/20☀️
Décimale: Masque de sous-réseau. . . . . . . . . : 255.255.240.0
```

☀️ Déso pas déso

```ladresse de réseau du LAN auquel vous êtes connectés en WiFi```
```
Adresse IP       : 00001010.00100001.01001001.01001101
Masque           : 11111111.11111111.11110000.00000000
☀️Adresse réseau   : 00001010.00100001.01000000.00000000 = 10.33.64.0.☀️
```
```
Adresse IP       : 00001010.00100001.01001001.01001101
Masque           : 00000000.00000000.00001111.11111111
☀️Broadcast        : 00001010.00100001.01001111.11111111 = 10.33.79.255☀️
```
```
adresses IP disponibles dans ce réseau : 4094 (2^20 = 4096 et 4096-2 =4094)
```
☀️ Hostname

```
PS C:\Users\vince> hostname
MSI
```

☀️ Passerelle du réseau

```
Passerelle par défaut. . . . . . . . . : 10.33.79.254
```
```
PS C:\Users\vince> arp -a
10.33.79.254          7c-5a-1c-d3-d8-76     dynamique
```

☀️ Serveur DHCP et DNS
Déterminer...
```
Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
```
```
Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

☀️ Table de routage

```
PS C:\Users\vince> netstat -r
 0.0.0.0          0.0.0.0     ☀️10.33.79.254☀️      10.33.73.77     30
```

II. Go further

☀️ Hosts ?

PS C:\Users\vince> ping b2.hello.vous

```
Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=15 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=15 ms TTL=55
Réponse de 1.1.1.1 : octets=32 temps=15 ms TTL=55

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 14ms, Maximum = 15ms, Moyenne = 14ms
```

☀️ Go mater une vidéo youtube et déterminer, pendant qu elle tourne...

```
2652	17.771089	10.33.73.77	91.68.245.78	UDP	77	60115 → 443 Len=35
```
```
Adresse IP: 91.68.245.78
```
```
Port serveur: 443
```
```
Port PC...: 60115
```

☀️ Requêtes DNS
Déterminer...

```
PS C:\Users\vince> nslookup www.thinkerview.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.thinkerview.com
Addresses:  2a06:98c1:3121::7
          2a06:98c1:3120::7
          ☀️188.114.97.7☀️
          188.114.96.7

PS C:\Users\vince> ping www.thinkerview.com
Envoi d’une requête 'ping' sur www.thinkerview.com [188.114.97.7] avec 32 octets de données :
Réponse de ☀️188.114.97.7☀️ : octets=32 temps=14 ms TTL=55
```
```
PS C:\Users\vince> nslookup 143.90.88.12
Serveur :   dns.google
Address:  8.8.8.8

Nom :    ☀️EAOcf-140p12.ppp15.odn.ne.jp☀️
Address:  143.90.88.12
```
.
☀️ Hop hop hop
Déterminer...

```
PS C:\Users\vince> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [172.67.74.226]
avec un maximum de 30 sauts :

  1     2 ms     2 ms     2 ms  10.33.79.254
  2     2 ms     2 ms     1 ms  145.117.7.195.rev.sfr.net [195.7.117.145]
  3     7 ms     2 ms     2 ms  237.195.79.86.rev.sfr.net [86.79.195.237]
  4     3 ms     3 ms     2 ms  196.224.65.86.rev.sfr.net [86.65.224.196]
  5    13 ms    10 ms    10 ms  164.147.6.194.rev.sfr.net [194.6.147.164]
  6     *        *        *     Délai d’attente de la demande dépassé.
  7     *        *        *     Délai d’attente de la demande dépassé.
  ☀️8☀️    25 ms    16 ms    15 ms  172.67.74.226
```

Itinéraire déterminé.
PS C:\Users\vince>


☀️ IP publique
Déterminer...

```
PS C:\Users\vince> (Invoke-WebRequest ifconfig.me/ip).Content
195.7.117.146
```

III. Le requin

☀️ Capture ARP

```
voir "Capture arp.pcapng"
```

☀️ Capture DNS
```
voir: capture DNS.pcapng
```

☀️ Capture TCP


📁 fichier tcp.pcap

voir: "capture tcp.pcapng"



