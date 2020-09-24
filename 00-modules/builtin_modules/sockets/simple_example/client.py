import socket

HOST = '127.0.0.1'
# HOST = socket.gethostname()
PORT = 1243
HEADERSIZE = 10


# connect to the server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# receive message from server
# client first expects to get a headersize information 

full_msg = ''
new_msg = True
while True:

    # get the message
    msg = s.recv(16).decode("utf-8")
    full_msg += msg


    if new_msg:
        print("new msg received")

        # get the length of the message
        message_len = int(msg[:HEADERSIZE])
        new_msg = False

    print("full message length: {0}".format(message_len))


    if len(full_msg) - HEADERSIZE == message_len:
        print("full msg received")
        
        # print message without fixed header size
        print(full_msg[HEADERSIZE:])
        new_msg = True
        full_msg = ""