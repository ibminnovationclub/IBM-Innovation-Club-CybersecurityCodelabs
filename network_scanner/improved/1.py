import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]

    print("IP\t\t\tMAC Address\n----------------------------------------------")
    #Create an empty list
    clients_list = []
    for element in answered_list:
        #create a dictionary that holds the mac and ip of each element
        client_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
        #add the client_dict as an element in clients_list
        clients_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

    print(clients_list)

scan("192.168.100.1/24")
