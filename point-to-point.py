from pyp2p.net import *
import time
import p2p
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
IP = s.getsockname()[0]
s.close()

import netifaces
print(netifaces.interfaces())

#>>> import socket
#>>> sock = socket.socket()
#>>> sock.bind(('', 0))
#>>> sock.getsockname()[1]
PORT = 4444c

# client app p2p app client ##############################################
#                                     p2p runas service/proc device-back
import client
##########################################################################
#
choice = input("Enter Choice Interface Number 0,1,2... : ")

from netifaces import AF_INET, AF_INET6, AF_LINK
for iface in netifaces.interfaces():
    if netifaces.ifaddresses(iface)[AF_INET][0]['addr'] == IP:
        INTE = str(netifaces.interfaces()[int(choice)])
        print(INTE)

from special_beta import auth as digest
IP_USER = str('testuser'+IP)
abc=digest.encode(IP_USER,'Sup3rS3cur3P4ssw0rd')
print(abc)

# Basic dGVzdHVzZXIxOTIuMTY4LjEwMS4xMTk6U3VwM3JTM2N1cjNQNHNzdzByZA==
# Basic dGVzdHVzZXIxOTIuMTY4LjEwMS4xMTE6U3VwM3JTM2N1cjNQNHNzdzByZA==

#Setup Bob's p2p node.
bob = Net(passive_bind=IP, passive_port=44445, interface=INTE, node_type="passive", debug=1)
bob.start()
bob.bootstrap()
bob.advertise()

#Event loop.
while 1:
    for con in bob:
        con.send_line("test")

    time.sleep(1)

from pyp2p.net import *
import time

#Setup Alice's p2p node.
alice = Net(passive_bind="192.168.0.45", passive_port=44444, interface="eth0:2", node_type="passive", debug=1)
alice.start()
alice.bootstrap()
alice.advertise()

#Event loop.
while 1:
    for con in alice:
        for reply in con:
            print(reply)

    time.sleep(1)
