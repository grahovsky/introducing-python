import xmlrpc.client
from time import sleep

proxy = xmlrpc.client.ServerProxy("http://localhost:6789/")

for i in range(5):
    result = proxy.getTime()
    print("Time is %s" % (result))
    sleep(1)

