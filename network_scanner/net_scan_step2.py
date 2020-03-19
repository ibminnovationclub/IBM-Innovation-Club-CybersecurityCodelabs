import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    #merge the two packets
    arp_request_broadcast = broadcast/arp_request


    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=2)
    #.srp returns two lists :(answered_packets & unanswered_packets)
    print(answered_list.summary())



scan("192.168.100.1/24")
