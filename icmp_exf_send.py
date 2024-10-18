import subprocess
import sys

# Vérifier que les bons arguments sont passés
if len(sys.argv) != 3:
    print("Usage: python icmp_exf_send.py <IP_destination> <caractère>")
    sys.exit(1)

destination_ip = sys.argv[1]
character = sys.argv[2]

# Vérifier que le caractère est un seul caractère
if len(character) != 1:
    print("Veuillez entrer un seul caractère.")
    sys.exit(1)

# Convertir le caractère en binaire
binary_char = character.encode('utf-8').hex()

# Construire la commande ping
command = ['ping', destination_ip, '-n', '1', '-l', str(len(binary_char)//2), binary_char]

# Exécuter la commande
try:
    subprocess.run(command, check=True)
    print(f"Caractère '{character}' envoyé à {destination_ip}.")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'envoi du ping : {e}")
