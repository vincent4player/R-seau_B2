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