import socket
from threading import Thread

PORT = 65535 # A Port Number
DATA_SIZE = 1024

def newClient_connect():
    with (connection):
        print("Connected through", address)

        while (True):
            data = connection.recv(DATA_SIZE)
            if (not data):
                break
    
            data = data.decode('ascii')
            print("Received message from ", address, ":", data)

            return_message = bytes(input(">_ "))
            
            connection.sendall(return_message, 'ascii')

# Setting up the socket server
"""
IP Address Format: 192.168.X.X
Local Network Format: 127.0.0.1 
"""
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(("", PORT))
socket.listen()

while (True):
    connection, address = socket.accept()

    # Create a thread to connect
    my_thread = Thread(target = newClient_connect, args = (connection, address))
