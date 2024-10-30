import socket
import re
import logging

def handle_client(client_socket):
    try:
        # get les donnés du client
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Message reçu du client : {data}")

       
        pattern = r'^(-?\d{1,5})\s*([+*-])\s*(-?\d{1,5})$'
        match = re.match(pattern, data)
        
        if match:
            num1, operator, num2 = match.groups()
            num1, num2 = int(num1), int(num2)

            # L'Opérations
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            else:
                result = "Opération non supportée"

            # Envoi du résultat
            client_socket.send(str(result).encode('utf-8'))
        else:
            client_socket.send("Opération invalide".encode('utf-8'))
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 13337))
    server.listen(5)
    print("Serveur en écoute sur le port 13337...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connexion de {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()