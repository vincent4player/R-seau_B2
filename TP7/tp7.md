TP7 SECU : Accès réseau sécurisé 
    
    
    
🌞Monter un serveur VPN Wireguard sur vpn.tp7.secu

```
[vincent@vpn ~]$ sudo modprobe wireguard 

[vincent@vpn ~]$ echo wireguard | sudo tee /etc/modules-load.d/wireguard.conf

[vincent@vpn ~]$ sudo cat /etc/sysctl.conf
# sysctl settings are defined through files in
# /usr/lib/sysctl.d/, /run/sysctl.d/, and /etc/sysctl.d/.
#
# Vendors settings live in /usr/lib/sysctl.d/.
# To override a whole file, create a new file with the same in
# /etc/sysctl.d/ and put new settings there. To override
# only specific settings, add a file with a lexically later
# name in /etc/sysctl.d/ and put new settings there.
#
# For more information, see sysctl.conf(5) and sysctl.d(5).
net.ipv4.ip_forward = 1
net.ipv6.conf.all.forwarding = 1

[vincent@vpn ~]$ sudo sysctl -p

[vincent@vpn ~]$ sudo dnf install wireguard-tools -y

[vincent@vpn ~]$ wg genkey | sudo tee /etc/wireguard/server.key

[vincent@vpn ~]$ sudo chmod 0400 /etc/wireguard/server.key

[vincent@vpn ~]$ sudo cat /etc/wireguard/server.key | wg pubkey | sudo tee /etc/wireguard/server.pub

[vincent@vpn ~]$ sudo mkdir -p /etc/wireguard/clients

[vincent@vpn ~]$ wg genkey | sudo tee /etc/wireguard/clients/john.key

[vincent@vpn ~]$ sudo chmod 0400 /etc/wireguard/clients/john.key

[vincent@vpn ~]$ sudo cat /etc/wireguard/clients/john.key | wg pubkey | tee /etc/wireguard/clients/john.pub

[vincent@vpn ~]$ sudo cat /etc/wireguard/wg0.conf
[Interface]
Address = 10.7.2.1/24
SaveConfig = false
PostUp = firewall-cmd --zone=public --add-masquerade
PostUp = firewall-cmd --add-interface=wg0 --zone=public
PostDown = firewall-cmd --zone=public --remove-masquerade
PostDown = firewall-cmd --remove-interface=wg0 --zone=public
ListenPort = 13337
PrivateKey = mGcIqApwPFcUngQUFKHINYQ4I02gFeCdmzvbOOnrYnM=

[Peer]
PublicKey = vZ/xzSCCSKBwvjaNz9bLZovgz2zFwza//5M2TupdOUs=
AllowedIPs = 10.7.2.11/32

[vincent@vpn ~]$ sudo firewall-cmd --add-port=13337/udp --permanent
success
[vincent@vpn ~]$ sudo firewall-cmd --reload

[vincent@vpn ~]$ sudo systemctl start wg-quick@wg0.service
```

```
🌞 Client Wireguard sur martine.tp7.secu

[vincent@vpn ~]$ sudo dnf install wireguard-tools

[vincent@vpn ~]$ sudo ip route del default via 10.0.2.1 dev enp0s8

[vincent@vpn ~]$ mkdir wireguard

[vincent@vpn ~]$ sudo cat wireguard/john.conf 
[Interface]
Address = 10.7.2.11/24
PrivateKey = gLkXDhHjnGY31EvUgd2oJDXFAynuVSioDM9zL954cm0=

[Peer]
PublicKey = +wPZCtpvc6FIKgKg7/MurbyS6Wt+qoRNfYRDg8N0RCk=
AllowedIPs = 0.0.0.0/0
Endpoint = 10.7.1.100:13337

[vincent@martine wireguard]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=57 time=27.3 ms
64 bytes from 1.1.1.1: icmp_seq=2 ttl=57 time=28.3 ms
```

🌞 Client Wireguard sur votre PC

```
Voir capture "WireguardPC.png"
```
```
Configuration client pc

[Interface]
PrivateKey = 6Ao53iaHyfQzmpnxWsvBZmttKGv2tXrJ5lRNHi1Hh10=
Address = 10.7.2.12/24

[Peer]
PublicKey = +wPZCtpvc6FIKgKg7/MurbyS6Wt+qoRNfYRDg8N0RCk=
AllowedIPs = 10.7.2.0/24
Endpoint = 10.7.1.100:13337
```
```
configuration vpn

[vincent@vpn ~]$ sudo nano /etc/wireguard/wg0.conf
[Interface]
Address = 10.7.2.1/24
SaveConfig = false
PostUp = firewall-cmd --zone=public --add-masquerade
PostUp = firewall-cmd --add-interface=wg0 --zone=public
PostDown = firewall-cmd --zone=public --remove-masquerade
PostDown = firewall-cmd --remove-interface=wg0 --zone=public
ListenPort = 13337
PrivateKey = mGcIqApwPFcUngQUFKHINYQ4I02gFeCdmzvbOOnrYnM=

[Peer]
PublicKey = vZ/xzSCCSKBwvjaNz9bLZovgz2zFwza//5M2TupdOUs=
AllowedIPs = 10.7.2.11/32

[Peer]
PublicKey = D+57POWpLJtnqRcICVhBX/nf3ivmZUSjMboEbpg8kTw=
AllowedIPs = 10.7.2.12/32
```

🌞 Ecrire un script client.sh

```
Voir "client.sh"
```

II. SSH
🌞 Générez des confs Wireguard pour tout le monde


[vincent@bastion ~]$ sudo ./client.sh
============================================
Clé publique générée pour le client :
6DWvBCucnaLjGcn5NgIWpwhAJB6hcSzEOcV9PmrX6Dg=
============================================
Ajoutez la clé suivante au fichier de configuration du serveur WireGuard :
--------------------------------------------
[Peer]
PublicKey = 6DWvBCucnaLjGcn5NgIWpwhAJB6hcSzEOcV9PmrX6Dg=
AllowedIPs = 10.7.2.91/32
--------------------------------------------
Ajout d'alias pour gérer l'interface VPN...
Démarrage de l'interface WireGuard...
[#] ip link add wg0-client type wireguard
[#] wg setconf wg0-client /dev/fd/63
[#] ip -4 address add 10.7.2.91/24 dev wg0-client
[#] ip link set mtu 1420 up dev wg0-client
[#] wg set wg0-client fwmark 51820
[#] ip -4 route add 0.0.0.0/0 dev wg0-client table 51820
[#] ip -4 rule add not fwmark 51820 table 51820
[#] ip -4 rule add table main suppress_prefixlength 0
[#] sysctl -q net.ipv4.conf.all.src_valid_mark=1
[#] nft -f /dev/fd/63
Ajout de la route par défaut via le serveur VPN...
Configuration terminée avec succès !
Le fichier client est disponible à l'adresse : /etc/wireguard/wg0-client.conf
[vincent@bastion ~]$ client_loop: send disconnect: Connection reset
PS C:\Users\vince> ssh vincent@10.7.1.12
vincent@10.7.1.12's password:
Last login: Mon Nov 25 17:34:38 2024
[vincent@bastion ~]$ ping 1.1.1.1
ping: connect: Network is unreachable
[vincent@bastion ~]$ sudo nano  /etc/wireguard/wg0-client.conf
[sudo] password for vincent:
[vincent@bastion ~]$ ping 1.1.1.1
ping: connect: Network is unreachable
[vincent@bastion ~]$ ping 1.1.1.1
PING 1.1.1.1 (1.1.1.1) from 10.7.2.189 client: 56(84) bytes of data.
64 bytes from 1.1.1.1: icmp_seq=1 ttl=254 time=19.5 ms
^C
--- 1.1.1.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 1003ms
rtt min/avg/max/mdev = 19.486/19.573/19.660/0.087 ms


🌞 Empêcher la connexion SSH directe sur web.tp7.secu

```
[vincent@web ~]$ sudo cat iptables.sh 
#!/bin/bash

iptables -F ; iptables -X

iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

iptables -A INPUT -p udp --sport 13337 -j ACCEPT
iptables -A OUTPUT -p udp --dport 13337 -j ACCEPT

iptables -A INPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT

iptables -A INPUT --src 10.7.2.1 -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT


[vincent@bastion ~]$ ssh 10.7.2.12
vincent@10.7.2.12's password: 
```

🌞 Connectez-vous avec un jump SSH

```
[vincent@bastion ~]$ ssh -J 10.7.2.12 10.7.2.13
vincent@10.7.2.12's password: 
vincent@10.7.2.13's password: 
Last login: Mon Nov 26 17:44:25 2024 from 10.7.2.1
[vincent@web ~]$ 
```

3. Connexion par clé
🌞 Générez une nouvelle paire de clés pour ce TP

```
PS C:\Users\vince> ssh-keygen -o -a 100 -t ed25519
Generating public/private ed25519 key pair.
Enter file in which to save the key (C:\Users\vince/.ssh/id_ed25519):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in C:\Users\vince/.ssh/id_ed25519
Your public key has been saved in C:\Users\vince/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:9G8pjI0cGWL/QBCUxIz+0Hs7Pgifj6+gLy4cllGJNJw vince@DESKTOP-6F93HS3
The key's randomart image is:
+--[ED25519 256]--+
|ooo .*=o         |
| E.o. +.         |
|  .. .o +        |
| .  o..= +       |
|  o  o .S .      |
| +  . o..O . .   |
|o . .o ++.= +    |
|.... .+.+  o     |
| ooo. o=+o       |
+----[SHA256]-----+
```

4. Conf serveur SSH
🌞 Changez l'adresse IP d'écoute

[vincent@web ~]$ sudo cat /etc/ssh/sshd_config | grep Listen
ListenAddress 10.7.2.1
[vicnent@web ~]$ sudo systemctl restart sshd
PS C:\Users\vince> ssh vincent@10.7.1.13
ssh: connect to host 10.7.1.13 port 22: Connection timed out

🌞 Améliorer le niveau de sécurité du serveur
```
Désactiver l'authentification par mot de passe dans /etc/ssh/sshd_config avec PasswordAuthentication no pour forcer l'utilisation des clés SSH.

Limiter l'accès à certains utilisateurs en ajoutant AllowUsers user1 user2 dans le même fichier de configuration, restreignant ainsi les connexions SSH.

Changer le port SSH par défaut avec Port 2222, ce qui diminue les risques liés aux attaques automatisées sur le port standard (22).
```

III. HTTP

1. Initial setup
🌞 Monter un bête serveur HTTP sur web.tp7.secu

```
sudo dnf install nginx 
sudo nano /etc/nginx/conf.d/web.conf
server {
    server_name web.tp7.secu;

    listen 10.7.2.1:80;

    root /var/www/site_nul;
}
sudo systemctl start nginx
sudo systemctl enable nginx
```

🌞 Site web joignable qu'au sein du réseau VPN

```
[vincent@web ~]$ sudo cat iptables.sh 
#!/bin/bash

iptables -F ; iptables -X

iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

iptables -A INPUT -p udp --sport 13337 -j ACCEPT
iptables -A OUTPUT -p udp --dport 13337 -j ACCEPT

iptables -A INPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT

iptables -A INPUT --src 10.7.2.1 -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT

iptables -A INPUT -i client -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 80 -j ACCEPT

iptables -L -v -n
```

🌞 Accéder au site web

```
PS C:\Users\vince> curl 10.7.2.13
<h1>toto</h1>
```

B. Génération du certificat pour le serveur web

🌞 Générer une clé et une demande de signature de certificat pour notre serveur web

```
[vincent@web ~]$ openssl req -new -nodes -out web.tp7.secu.csr -newkey rsa:4096 -keyout web.tp7.secu.key
........+...+...+..........+.....+......+.+.........+.....+...+.......+...........+...+.+...+.....+.+......+........+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...+.....+.+....................+.+.........+...+..+...+...+...+......+.+............+..+...+.+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+......+......+............+.......+.......................+...+...+.+...............+...........+.......+..+.+..+......+......................+.................+.+....................+....+..+...................+..+...+.+.....+......+....+...+........+.......+...+.....+.............+......+...+...+...+..............+.......+.....+...+.+.....+......+.+..+.............+...+..+.........+...+.......+...+............+......+..................+...........+.+........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
........+....+..+.+..+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*.+....+.........+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*...+......+.......+........+..........+..+...+...+.+........+.......+.....................+..+.......+..............+...................+......+.....+.....................+....+......+........+.+.........+..................+.................+...............+......+..........+......+...+.................................+........+...............+......+....+..+.......+.....+......+....+.....+.+.....+.+...+...+..+.......+.....+......+..........+........+.+...+...+..............+.+.....+....+.....+......+..........+...+.....+.+...+.................+......+....+...........+....+.....+....+.....+.......+.................+...+..........+...+..............+.......+.....+..........+.............................+....+...+.................+...+...............+.......+...........+.+..................+.....................+.........+......+..+....+.........+............+.....+.........+....+............+...+.....+.......+..+.......+...+..+...............+...+.......+...+..+...+..................+...+....+.....+.+...........+...+...+..................+....+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [XX]:fr
State or Province Name (full name) []:bordeaux
Locality Name (eg, city) [Default City]:bordeaux
Organization Name (eg, company) [Default Company Ltd]:vicnent
Organizational Unit Name (eg, section) []:ynov
Common Name (eg, your name or your server's hostname) []:vincent
Email Address []:le vince

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:root
An optional company name []:root
[vincent@web ~]$
```

🌞 Faire signer notre certificat par la clé de la CA

```
[vincent@web ~]$ sudo cat v3.ext
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = web.tp7.secu
DNS.2 = www.tp7.secu
[vincent@web ~]$ openssl x509 -req -in web.tp7.secu.csr -CA CA.pem -CAkey CA.key -CAcreateserial -out web.tp7.secu.crt -days 500 -sha256 -extfile v3.ext
Certificate request self-signature ok
subject=C = fr, ST = bordeaux, L = bordeaux, O = vicnent, OU = ynov, CN = vincent, emailAddress = le vince
Enter pass phrase for CA.key:
```
C. Bonnes pratiques RedHat
🌞 Déplacer les clés et les certificats dans l'emplacement réservé

```
[vincent@web ~]$ sudo mv CA.key CA.pem web.tp7.secu.key /etc/pki/tls/private/
[vincent@web ~]$ sudo mv CA.srl web.tp7.secu.crt web.tp7.secu.csr /etc/pki/tls/certs/
```

D. Config serveur Web
🌞 Ajustez la configuration NGINX

```
[vincent@web ~]$ sudo cat /etc/nginx/conf.d/web.conf 
server {
    server_name web.tp7.secu;

    listen 10.7.2.103:443 ssl;

    ssl_certificate /etc/pki/tls/certs/web.tp7.secu.crt;
    ssl_certificate_key /etc/pki/tls/private/web.tp7.secu.key;

    root /var/www/site_nul;

    location / {
        index index.html index.htm;
    }
}
```