import socket
"""
Connects to Ms. Mia's online server.

Local IP Address: 192.168.68.120
Ms. Mia's IP Adress: 107.190.76.212
"""

HOST_IP = '107.190.76.212'
PORT = 65432
DATA = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as (s):
    s.connect((HOST_IP, PORT))

    # Initial state of message
    data = s.recv(DATA)
    print(data.decode('ascii'))

    while (True):
        # Send input
        message = input('>_: ')
        message = bytes(message, 'ascii')
        s.sendall(message)

        # Receive input * 2
        data = s.recv(DATA)
        print(data.decode('ascii'))

        data = s.recv(DATA)
        print(data.decode('ascii'))