Compte-rendu
☀️ Sur node1.lan1.tp2
```
afficher ses cartes réseau
```
```
[vincent@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:56:01:3f brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s3
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe56:13f/64 scope link
       valid_lft forever preferred_lft forever
[vincent@node1 ~]$
```
```
afficher sa table de routage
```
```
[vincent@node1 ~]$ ip route show
10.1.1.0/24 dev enp0s3 proto kernel scope link src 10.1.1.11 metric 100
10.1.2.0/24 via 10.1.1.254 dev enp0s3
[vincent@node1 ~]$
```
```
prouvez qu'il peut joindre node2.lan2.tp2
```
```
[vincent@node1 ~]$ ping 10.1.2.12
PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=1.76 ms
64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=1.43 ms
^C
--- 10.1.2.12 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 1.430/1.595/1.761/0.165 ms
[vincent@node1 ~]$
```
```
prouvez avec un traceroute que le paquet passe bien par router.tp2
```
```
[vincent@node1 ~]$ traceroute 10.1.2.12
traceroute to 10.1.2.12 (10.1.2.12), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  6.775 ms  6.468 ms  0.658 ms
 2  10.1.2.12 (10.1.2.12)  1.795 ms !X  1.352 ms !X  1.758 ms !X
[vincent@node1 ~]$
```

II. Interlude accès internet
☀️ Sur router.tp2

```
prouvez que vous avez un accès internet (ping d'une IP publique)

[vincent@router ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=19.5 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=113 time=19.3 ms
^C
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 19.319/19.421/19.523/0.102 ms
[vincent@router ~]$
```
```
prouvez que vous pouvez résoudre des noms publics (ping d'un nom de domaine public)

[vincent@router ~]$ ping youtube.com
PING youtube.com (142.250.179.110) 56(84) bytes of data.
64 bytes from par21s20-in-f14.1e100.net (142.250.179.110): icmp_seq=1 ttl=116 time=20.3 ms
64 bytes from par21s20-in-f14.1e100.net (142.250.179.110): icmp_seq=2 ttl=116 time=20.1 ms
^C
--- youtube.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 20.086/20.184/20.282/0.098 ms
[vincent@router ~]$
```

☀️ Accès internet LAN1 et LAN2

```
ajoutez une route par défaut sur les deux machines du LAN1

[vincent@node2 ~]$ sudo ip route add default via 10.1.1.254
[sudo] password for vincent:
[vincent@node2 ~]$
```
```
configurez l'adresse d'un serveur DNS que vos machines peuvent utiliser pour résoudre des noms
dans le compte-rendu, mettez-moi que la conf des points précédents sur node2.lan1.tp2
prouvez que node2.lan1.tp2 a un accès internet :

il peut ping une IP publique
il peut ping un nom de domaine public
```
```
[vincent@node2 ~]$  sudo nano /etc/resolv.conf
[sudo] password for vincent:
[vincent@node2 ~]$ ping youtube.com
PING youtube.com (142.250.179.110) 56(84) bytes of data.
64 bytes from par21s20-in-f14.1e100.net (142.250.179.110): icmp_seq=1 ttl=115 time=21.1 ms
64 bytes from par21s20-in-f14.1e100.net (142.250.179.110): icmp_seq=2 ttl=115 time=20.5 ms
^C64 bytes from 142.250.179.110: icmp_seq=3 ttl=115 time=21.8 ms

--- youtube.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 10100ms
rtt min/avg/max/mdev = 20.505/21.148/21.810/0.532 ms
[vincent@node2 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=112 time=21.5 ms
^C
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 21.518/21.518/21.518/0.000 ms
[vincent@node2 ~]$
```

III. Services réseau


☀️ Sur web.lan2.tp2

```
[vincent@web ~]$ sudo dnf -y install nginx
[vincent@web var]$ sudo nano /var/www/site_nul/index.html
<h1>Test <3</h1>

[vincent@web ~]$ sudo nano /etc/nginx/conf.d/site_nul.conf
```
```
Config:
```
```
server {
    listen 80;

    location / {
        root /var/www/site_nul/;
        index index.html index.htm;
    }
}
```
```
[vincent@web ~]$ sudo systemctl start nginx
[vincent@web ~]$ sudo systemctl enable nginx

[vincent@web var]$ sudo firewall-cmd --add-port=80/tcp --permanent
[vincent@web var]$ sudo firewall-cmd --reload

[vincent@web site_nul]$ ss -alntupe | grep 80
tcp   LISTEN 0      511          0.0.0.0:80        0.0.0.0:*    ino:23440 sk:4 cgroup:/system.slice/nginx.service <->
tcp   LISTEN 0      511             [::]:80           [::]:*    ino:23441 sk:6 cgroup:/system.slice/nginx.service v6only:1 <->

[vincent@web ~]$ sudo firewall-cmd --list-all
[sudo] password for vincent:
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s3
  sources:
  services: cockpit dhcpv6-client ssh
  ports: 80/tcp
  protocols:
  forward: yes
  masquerade: no
  forward-ports:
  source-ports:
  icmp-blocks:
  rich rules:
  ```

☀️ Sur node1.lan1.tp2

```
[vincent@node1 ~]$ sudo cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.1.2.12 site_nul.tp2

[vincent@node1 ~]$ curl site_nul.tp2
<h1>Test <3</h1>
```

