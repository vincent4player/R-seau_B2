from scapy.all import sniff

def tcp_syn_ack(packet):
    if packet.haslayer('TCP') and packet['TCP'].flags == 'SA':  
        print("TCP SYN ACK reçu !")
        print(f"- Adresse IP src : {packet['IP'].src}")
        print(f"- Adresse IP dst : {packet['IP'].dst}")
        print(f"- Port TCP src : {packet['TCP'].sport}")
        print(f"- Port TCP dst : {packet['TCP'].dport}")
        return True  

sniff(filter="tcp", prn=tcp_syn_ack, count=1)
