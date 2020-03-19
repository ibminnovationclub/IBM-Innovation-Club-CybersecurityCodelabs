import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request

    #cleaning the output verbose=False
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]

#we print header outside loop to print it only once
    print("IP\t\t\tMAC Address\n----------------------------------------------")
    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("-----------------------------------------------------------------------------------------------")

scan("192.168.100.1/24")
