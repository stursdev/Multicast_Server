#! /usr/bin/env python3

# Server-side
# Name: Sam Tursunov
# This is the server side of our application
# The server has two sockets. One for receiving and one for sending multicast messages to all clients.


import socket
import struct

mcast_group = ('224.2.2.2', 30001)
server = ('', 30000)

# Create a send socket
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Create receive socket
recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the receiving socket
recv_sock.bind(server)

print("Starting Server...")
msg = 'Connected! Waiting for msgs...'
server_sock.sendto(msg.encode(), (mcast_group))


while True:
    print("Waiting to recieve...")
    data, address = recv_sock.recvfrom(1024)
    msg = data.decode()
    print("Received: " + msg + " from " + str(address))
    print("Multicasting Received Msg...")
    server_sock.sendto(msg.encode(), mcast_group)
