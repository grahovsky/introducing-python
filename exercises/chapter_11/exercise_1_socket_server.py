from datetime import datetime
import socket

address = ('localhost', 6789)
max_size = 4096

print('Starting the server at', datetime.now())
print('Waiting for a client to call.')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)

client, addr = server.accept()
dataIn = client.recv(max_size)

if dataIn == b'time':
    now = str(datetime.utcnow())
    dataOut = now.encode('utf-8')
    client.sendall(dataOut)
    client.close()

server.close()