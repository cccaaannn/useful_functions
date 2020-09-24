import socket
import time


HOST = '127.0.0.1'
# HOST = socket.gethostname()
PORT = 1243
HEADERSIZE = 10


# start the server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)



# wait for client connections
clientsocket, address = s.accept()
print("Connection from {0} has been established.".format(address))

# send message to client
message = "Welcome to the server!"
message = f"{len(message):<{HEADERSIZE}}" + message
clientsocket.send(bytes(message,"utf-8"))


# send time information to client 
# we sent a fixed sized header size first let the client know about the size of the message 
while True:
    time.sleep(3)
    message = f"The time is {time.time()}"
    message = f"{len(message):<{HEADERSIZE}}"+message
    clientsocket.send(bytes(message,"utf-8"))
