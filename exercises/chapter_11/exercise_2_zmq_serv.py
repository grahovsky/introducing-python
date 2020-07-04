import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))

while True:
    # Wait for next request from client
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')

    print("That voice in my head says: %s" % request_str)

    if request_str == 'time':
        reply_str = str(datetime.utcnow())
        reply_bytes = bytes(reply_str, 'utf-8')
        server.send(reply_bytes)
