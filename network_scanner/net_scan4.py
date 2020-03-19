import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()

    #merge the two packets
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

scan("192.168.100.1/24")
