import socket
import time
import pickle


HOST = '127.0.0.1'
PORT = 1243
HEADERSIZE = 10

# start the server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    # wait for client connections
    clientsocket, address = s.accept()
    print("Connection from {0} has been established.".format(address))

    # convert python object to byte
    d = {1:"hi", 2: "there"}
    message = pickle.dumps(d)

    # add the header and send the object as bytes
    message = bytes(f"{len(message):<{HEADERSIZE}}", 'utf-8') + message
    print(message)
    clientsocket.send(message)
