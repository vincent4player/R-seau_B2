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




☀️ IP publique
Déterminer...

l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)


III. Le requin
Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format .pcap donc.
Faites clean 🧹, vous êtes des grands now :

livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour

vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark


stockez les fichiers .pcap dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :


[Lien vers capture ARP](./captures/arp.pcap)



☀️ Capture ARP


📁 fichier arp.pcap

capturez un échange ARP entre votre PC et la passerelle du réseau
vous pouvez vider votre table ARP à l'aide d'une commande, pour forcer l'échange ARP


En bref rappel : pour communiquer avec quelqu'un sur un LAN, il faut connaître son adresse MAC. Vous avez tout le temps besoin de communiquer avec le routeur, car c'est lui qui fait passer vos paquets vers internet. Il est donc nécessaire d'apprendre l'adresse MAC du routeur. Votre PC fait un échange ARP pour apprendre la MAC de quelqu'un sur son LAN, comme le routeur.


☀️ Capture DNS


📁 fichier dns.pcap

capturez une requête DNS vers le domaine de votre choix et la réponse
vous effectuerez la requête DNS en ligne de commande


☀️ Capture TCP


📁 fichier tcp.pcap

effectuez une connexion qui sollicite le protocole TCP
je veux voir dans la capture :

un 3-way handshake
un peu de trafic
la fin de la connexion TCP




TCP est le protocole qu'on va trouver DANS les paquets IP. Un paquet IP achemine le message jusqu'à une certaine machine, qui peut ouvrir le paquet IP afin de voir un message TCP. Le contenu du message TCP (une requête HTTP par exemple) est alors envoyé à une application (un serveur web par exemple) pour qu'elle traite le contenu.




Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈