# this script will send multicast traffic
#
#


#!/usr/bin/env python
#import modules needed for script
import socket

MCAST_GRP = '225.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
pac = 0

while pac < 100000:
	
	sock.sendto("mcast packet being sent", (MCAST_GRP, MCAST_PORT))
	pac = pac + 1
        print " packets done"	
	
