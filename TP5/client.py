import socket
import re
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("client")


host = '10.33.49.113'
port = 13337

def main():
    try:
        # Créer le socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        logger.info("Connexion au serveur %s:%d réussie", host, port)

        # le pattern de l'operation (parfaite)
        pattern = r'^(-?\d{1,5})\s*([+*-])\s*(-?\d{1,5})$'
        while True:
            user_input = input("Veuillez saisir une opération arithmétique : ")
            if re.match(pattern, user_input):
                break  # si l'entrée est valide on BREAK
            else:
                logger.error("Format invalide. Utilisez seulement les signes (-,+,*) et des nombres entre -100000 et +100000")

        # Envoyer l'opération au serveur
        client_socket.sendall(user_input.encode('utf-8'))
        logger.info("Opération envoyée au serveur : %s", user_input)

        # c'est le resultat de server 
        result = client_socket.recv(1024).decode('utf-8')
        print("Résultat reçu du serveur :", result)

    except socket.error as e:
        logger.error("Erreur de connexion au serveur : %s", e)
        sys.exit(1)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
