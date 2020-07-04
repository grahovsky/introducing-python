import socket
from datetime import datetime

address = ('localhost', 6789)
max_size = 4096

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(b'time')

data = client.recv(max_size)
print('Client read', data)
client.close()
