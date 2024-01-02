import socket
"""
Connects to Ms. Mia's online server.

Local IP Address: 
Ms. Mia's IP Adress:
"""

DATA_SIZE = 1024
HOST_IP = ''
PORT = 65432

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST_IP, PORT))

while (True):
    message = input(">_: ")
    message = bytes(message, 'ascii')
    socket.sendall(message)

    data = socket.recv(DATA_SIZE)
