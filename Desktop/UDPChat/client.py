#! /usr/bin/env python3

# Client-side
# Name: Sam Tursunov
# This client will ask the user to type their handle name and then ask them to type a msg
# The client application will send the handle name + user message to the server and receive multicast messages

from tkinter import *
import socket
import struct
import urllib.request

# Multicast Address
mcast_addr = '224.2.2.2'
mcast_port = 30001
mcast_server = ('', 30001)

# Create UDP socket that will listen to multicast messages
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the UDP socket
client_sock.bind(mcast_server)

# Add the socket to the multicast group on all interfaces
group = socket.inet_aton(mcast_addr)
mreq = struct.pack('4sl', group, socket.INADDR_ANY)
client_sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print("Starting Client...")
print("Waiting to connect...")

data, address = client_sock.recvfrom(1024)
print(data.decode() + " from " + str(address))
user_handle = input("Type your name handle: ")


while True:
    user_msg = input("Type Msg: ")
    send_msg = user_handle + user_msg
    server = ('137.142.101.120', 30000) # Server address = IP of machine where server is running
    # Create a UDP socket that will be used to send a message to the server
    send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_sock.sendto(send_msg.encode(), server)
    send_sock.close()
    print("Msg sent!")
    data, address = client_sock.recvfrom(1024)
    print(data.decode())
    
    

