from xmlrpc.server import SimpleXMLRPCServer

def getTime():
    from datetime import datetime
    data = str(datetime.utcnow())
    print('Server sent', data)
    return data

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(getTime, "getTime")
server.serve_forever()
