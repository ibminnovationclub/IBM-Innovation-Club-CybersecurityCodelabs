import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.168.100.1/24")


