#!/usr/bin/env python

import subprocess
import optparse

def get_arguments():
	#creating instance of a class
	parser = optparse.OptionParser()

	#the first argument it can accept from the users
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")interface = input("interface > ")

	#Pass the arguments it gets
	(options, arguments) = parser.parse_args()

	#check if options contain a value for the interface and mac address
	if not  options.interface:
		#code to handle error
		parse.error("[-] Please specify an interface, use --help for more info.")
	elif not options.new_mac:
		#code to handle error
		parse.error("[-] Please specify a new_mac, use --help for more info.")
	return options
def change_mac(interface, new_mac):
	print("[+] Changing MAC address for " + interface " to " + new_mac")

	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
#Calling change_mac function with direct inputs
change_mac(options.interface, options.new_mac)

