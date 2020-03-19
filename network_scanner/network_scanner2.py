import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst= ip
    print(arp_request.summary())


scan("192.168.100.2/24")
