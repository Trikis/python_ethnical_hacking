#!/usr/bin/env python3

import scapy.all as scapy
import optparse

def is_ip_adress(ip):
    ip_list = ip.split(".")
    #192.168.0.1
    if len(ip_list) != 4:
        print("[-] Incorrect ip\n")
        exit()
    for elem in ip_list:
        for symbol in elem:
            if not (ord("0") <= ord(symbol) <= ord("9")):
                print("[-] Incorrect ip\n")
                exit()
        if elem[0] == '0' and len(elem) > 1:
            print("[-] Incorrect ip\n")
            exit()
        number = int(elem)
        if not (0 <= number <= 255):
            print("[-] Incorrect ip\n")
            exit()
    return True

def get_argumnets():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--ip", dest = "ip",help="IP / IP range")
    arguments, options = parser.parse_args()

    if not arguments.ip:
        parser.error("[-] Please set IP adress, for more information use --help")
    return str(arguments.ip)

def parse_arguments(ip_argument):
    head ,left, right , = "", None, None
    if ip_argument.find("-") == -1:
        is_ip_adress(ip_argument)
        head = ip_argument[:ip_argument.rfind(".")]
        left = int(ip_argument[ip_argument.rfind(".") + 1:])
        right = left
    else:
        ip_list = ip_argument.split("-")
        if len(ip_list) != 2:
            print("[-] Inccorrect IP range,example of correct 192.168.0.1-192.168.0.100")
            exit()
        is_ip_adress(ip_list[0])
        head1 = ip_list[0][:ip_list[0].rfind(".")]

        is_ip_adress(ip_list[1])
        head2 = ip_list[1][:ip_list[1].rfind(".")]

        if head1 != head2:
            print("[-] Incorrect IP range(u can use only mask = 24 bytes), for example 192.168.0.1-192.168.0.100")
            exit()
        head = head1
        
        left = int(ip_list[0][ip_list[0].rfind(".") + 1:])
        right = int(ip_list[1][ip_list[1].rfind(".") + 1:])

        if left > right:
            print("[-] Incorrect IP range, example of correct range: 192.168.0.1-192.168.0.100")
            exit()
        
        return head,left,right

def scan(head,left,right):
    print("IP Adress\t\t\tMAC Adress\n----------------------------------------------")
    for curr in range(left,right + 1):
        ip_string = head + "." + str(curr)

        ip_request = scapy.ARP(pdst = ip_string)
        ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

        ether_ip_request = ether / ip_request
        answered_list = scapy.srp(ether_ip_request,timeout = 0.2, verbose = False)[0]
        
        for elem in answered_list:
            print(elem[1].psrc + "\t\t" + elem[1].hwsrc)
    



head,left,right = parse_arguments(get_argumnets())
scan(head,left,right)

        
