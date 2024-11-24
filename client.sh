#!/bin/bash

# Vérifiez si vous êtes root, sinon demandez un mot de passe pour escalader les privilèges
if [ "$(id -u)" -ne 0 ]; then
  echo "Ce script doit être exécuté avec des privilèges root." 
  sudo "$0" "$@"
  exit
fi

# 🌞 Vérifier si WireGuard est installé, sinon installer
if ! command -v wg-quick &> /dev/null; then
  echo "WireGuard n'est pas installé. Installation des outils WireGuard..."
  dnf install -y wireguard-tools
else
  echo "WireGuard est déjà installé."
fi

# 🌞 Générer la clé privée et la clé publique si elles n'existent pas
if [ ! -f /etc/wireguard/client.key ]; then
  echo "Génération de la clé privée..."
  wg genkey | sudo tee /etc/wireguard/client.key
  echo "Définition des permissions restrictives sur la clé privée..."
  sudo chmod 0400 /etc/wireguard/client.key
else
  echo "La clé privée existe déjà."
fi

if [ ! -f /etc/wireguard/client.pub ]; then
  echo "Génération de la clé publique..."
  sudo cat /etc/wireguard/client.key | wg pubkey | sudo tee /etc/wireguard/client.pub
else
  echo "La clé publique existe déjà."
fi

# 🌞 Créer le répertoire wireguard dans le répertoire personnel si nécessaire
mkdir -p ~/wireguard

# 🌞 Créer le fichier de configuration WireGuard
CONFIG_FILE=~/wireguard/john.conf

if [ ! -f "$CONFIG_FILE" ]; then
  echo "Création du fichier de configuration WireGuard..."

  # Clé publique du serveur
  SERVER_PUBLIC_KEY="+wPZCtpvc6FIKgKg7/MurbyS6Wt+qoRNfYRDg8N0RCk="

  # Créer la configuration dans le fichier john.conf
  cat <<EOL > $CONFIG_FILE
[Interface]
Address = 10.7.1.20/24
PrivateKey = $(cat /etc/wireguard/client.key)

[Peer]
PublicKey = $SERVER_PUBLIC_KEY
AllowedIPs = 0.0.0.0/0
Endpoint = 10.7.1.100:13337
EOL

  echo "Configuration écrite dans $CONFIG_FILE"
else
  echo "Le fichier de configuration existe déjà."
fi

# 🌞 Ajouter un alias 'vpn' pour se connecter au VPN
echo "Ajout d'un alias 'vpn' pour se connecter au VPN..."

# Vérifiez si l'alias est déjà dans .bashrc
if ! grep -q "alias vpn=" ~/.bashrc; then
  echo "alias vpn='sudo wg-quick up ~/wireguard/john.conf'" >> ~/.bashrc
  echo "Alias 'vpn' ajouté dans ~/.bashrc."
else
  echo "L'alias 'vpn' existe déjà dans ~/.bashrc."
fi

# 🌞 Ajouter la route par défaut via le VPN
echo "Ajout de la route par défaut via le VPN..."
sudo ip route add default dev wg0

# 🌞 Sourcez .bashrc pour que l'alias prenne effet immédiatement
source ~/.bashrc

echo "Alias 'vpn' ajouté et la route par défaut sera ajoutée automatiquement au démarrage."
echo "Vous pouvez maintenant vous connecter au VPN en utilisant la commande 'vpn' dans votre terminal."

