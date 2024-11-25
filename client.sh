#!/bin/bash

# Vérification des permissions root
if [ "$(id -u)" -ne 0 ]; then
    echo "Ce script nécessite les privilèges root. Veuillez réessayer en tant qu'utilisateur root."
    exit 1
fi

# Vérification de l'installation de WireGuard
if ! command -v wg &> /dev/null; then
    echo "WireGuard n'est pas disponible sur ce système. Installez-le pour continuer."
    exit 1
fi

# Génération des clés WireGuard
PRIVATE_KEY=$(wg genkey)
PUBLIC_KEY=$(echo "$PRIVATE_KEY" | wg pubkey)

# Génération d'une adresse IP aléatoire pour le client
CLIENT_IP_SUFFIX=$((10 + RANDOM % 245))
SERVER_IP="10.7.2.1"

# Création du fichier de configuration client
CONFIG_PATH="/etc/wireguard/wg0-client.conf"
cat > "$CONFIG_PATH" <<CONFIG
[Interface]
PrivateKey = $PRIVATE_KEY
Address = 10.7.2.${CLIENT_IP_SUFFIX}/24

[Peer]
PublicKey = +wPZCtpvc6FIKgKg7/MurbyS6Wt+qoRNfYRDg8N0RCk=
AllowedIPs = 0.0.0.0/0
Endpoint = 10.7.1.100:13337
CONFIG

# Instructions pour l'utilisateur
echo "============================================"
echo "Clé publique générée pour le client :"
echo "$PUBLIC_KEY"
echo "============================================"
echo "Ajoutez la clé suivante au fichier de configuration du serveur WireGuard :"
echo "--------------------------------------------"
echo "[Peer]"
echo "PublicKey = $PUBLIC_KEY"
echo "AllowedIPs = 10.7.2.${CLIENT_IP_SUFFIX}/32"
echo "--------------------------------------------"

# Création d'alias pour simplifier l'utilisation
echo "Ajout d'alias pour gérer l'interface VPN..."
sleep 2
{
    echo "alias start-vpn='wg-quick up wg0-client'"
    echo "alias stop-vpn='wg-quick down wg0-client'"
} >> ~/.bash_aliases
source ~/.bash_aliases

# Activation de l'interface et configuration de la route
echo "Démarrage de l'interface WireGuard..."
sleep 2
wg-quick up wg0-client

echo "Ajout de la route par défaut via le serveur VPN..."
sleep 2
ip route add default via "$SERVER_IP"

# Fin du script
echo "Configuration terminée avec succès !"
echo "Le fichier client est disponible à l'adresse : $CONFIG_PATH"
