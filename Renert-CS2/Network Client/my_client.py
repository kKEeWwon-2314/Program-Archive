import socket
"""
Connects to Ms. Mia's online server.

Local IP Address: 192.168.68.120
Ms. Mia's IP Adress: 107.190.76.212
"""

DATA_SIZE = 1024
HOST_IP = '107.190.76.212'
PORT = 65432

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST_IP, PORT))

while (True):
    message = input(">_: ")
    message = bytes(message, 'ascii')
    socket.sendall(message)

    data = socket.recv(DATA_SIZE)
