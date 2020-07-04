import socket
print(socket.gethostbyname('www.crappytaxidermy.com'))

print(socket.getservbyname('http'))

for i in range(1, 100):
    try:
        print("{}".format(i), socket.getservbyport(i))
    except:
        pass