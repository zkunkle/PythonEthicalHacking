#!/usr/bin/env python
import subprocess
import optparse

def get_arguments():
    # user prompt for the interface name and MAC address

    parser = optparse.OptionParser()

    # the user can provide -i or --interface in the command
    parser.add_option("-i", "--interface", dest="interface", help="Please input the interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Please input the new MAC address")

    # parse_args allows the object to understand what the user has entered and returns the arguments/values to a variable. For example, options.newMac will grab the newMac variable
    (options, arguments) =  parser.parse_args()
    if not options.interface:
        # if the user did not put in a value for interface
        parser.error("ERROR: Please specify an interface. Use --help for more information")
    elif not options.new_mac:
        # if the user did not put in a value for new_mac
        parser.error("ERROR: Please specify a new MAC address. Use --help for more information")
    return options

def mac_changer(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Call the functions above
# get_arguments will return anything from parser.parse_args()
options = get_arguments()
mac_changer(options.interface, options.new_mac)