import socket
"""
Connects to Ms. Mia's online server.

Local IP Address: 
Ms. Mia's IP Adress: 
"""

HOST_IP = '' # Obviously im not gonna show my IP address
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
