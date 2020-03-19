#!/usr/bin/env python

import subprocess
import optparse

#creating instance of a class
parser = optparse.OptionParser()

#the first argument it can accept from the users
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")interface = input("interface > ")

#Pass the arguments it gets
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_macinterface = input("interface > ")

print("[+] Changing MAC address for " + interface " to " + new_mac")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

