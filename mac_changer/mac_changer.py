#!/usr/bin/env python3
import subprocess
import optparse
import re


def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="Your interface")
    parse.add_option("-m","--mac",dest="new_mac",help="New MAC Adress")

    arguments,options = parse.parse_args()

    if not arguments.interface:
        parse.error("Please enter your enterface")
    elif not arguments.new_mac:
        parse.error("Please enter your new MAC adress")
    return arguments

def change_mac(interface,new_mac):
    print("Staring changing MAC for interface:{0} to {1}".format(interface,new_mac))
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig",interface]))
    mac_adres_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
    if mac_adres_search_result:
        return mac_adres_search_result.group(0)
    else:
        print("[-] Could not rad MAC adress")


arguments = get_arguments()
current_mac = get_current_mac(arguments.interface)
print("Current MAC: "+ str(current_mac))

change_mac(arguments.interface,arguments.new_mac)

current_mac = get_current_mac(arguments.interface)
if current_mac == arguments.new_mac:
    print("MAC adrees was changed to {0}".format(current_mac))
else:
    print("[-]MAC adress  did not get changed")
    
