# Multicast_Server

This is a UDP Multicast Client Server Application

File client.py will run the client side of the application. The client.py file will need to edited to use the IP address of the machine running the server.py file. The users running client.py file will be prompted to enter a handle name and then a message. The client will send the message to the server and receive multicast messages.

File server.py will run the server side of the application. The server will receive messages from clients and then Multicast the messages to all users running the client application.

This program used UDP socket programming.
