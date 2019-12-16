#!/usr/bin/env python2

import sh
import os
import platform

#Asks for IP input
net = raw_input("Enter the Network Address: ")

#Parses input by separating at the dots
net1= net.split('.')
print net1
a = '.'

#Re-adds dots and removes last octal of input IP
net2 = net1[0] + a + net1[1] + a + net1[2] + a
print net2

#Asks for IP range
#st1 = int(input("Enter the Starting Number: "))
st1 = int(raw_input("Enter the Starting Number: "))
#en1 = int(input("Enter the Last Number: "))
en1 = int(raw_input("Enter the Last Number: "))
#en1 = en1 + 1


# Pings IP addresses within given ranges
# Uncomment lines with 'print "no response from", addr', if hosts that do not respond should be printed.
# Comment out 'pass' if hosts that do not respond should be printed
for ip in range(st1, en1):
	addr = net2 + str(ip)
	oper = platform.system()
	if (oper == "Windows"):
		try: 
			sh.ping(addr, "-n 1", _out="/dev/null")
			print "Host", addr, "is up"
		except sh.ErrorReturnCode_1:
			#print "no response from", addr
			pass
	elif (oper == "Linux"):
		try: 
			sh.ping(addr, "-c 1", _out="/dev/null")
			print "Host", addr, "is up"
		except sh.ErrorReturnCode_1:
			#print "no response from", addr
			pass
	else:
		try: 
			sh.ping(addr, "-c 1", _out="/dev/null")
			print "Host", addr, "is up"
		except sh.ErrorReturnCode_1:
			#print "no response from", addr
			pass


print ("Scanning Completed")



