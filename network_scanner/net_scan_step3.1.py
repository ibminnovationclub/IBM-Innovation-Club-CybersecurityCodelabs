import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request

    #save only the first element [0] to answered_list
    answered_list = scapy.srp(arp_request_broadcast, timeout=5)[0]

    #for each packet in answered_list print packet
    for element in answered_list:
        #answered_list has a list within it, (packetsent[0], answer[1])
        print(element[1].show())
        print("-----------------------------------------------------------------------------------------------")

scan("192.168.100.1/24")
