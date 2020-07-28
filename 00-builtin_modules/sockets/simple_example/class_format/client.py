import socket


class client():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_client_options()
        self.client_socket.connect((self.SERVER_IP, self.SERVER_PORT))

        self.is_running = False
        self.messages = []
        self.current_message = ""
        self.current_message_temp = ""
        self.current_message_len = 0

    def set_client_options(self, SERVER_IP = "127.0.0.1", SERVER_PORT = 1243, HEADERSIZE = 10):
        self.SERVER_IP = SERVER_IP
        self.SERVER_PORT = SERVER_PORT
        self.HEADERSIZE = HEADERSIZE
        self.HEADERSIZE_ENLARGED = self.HEADERSIZE + 5  # enlarged header size to be extra safe 
        
    def __str__(self):
        temp_str = ""
        for message in self.messages:
            temp_str += message
        return temp_str

    def run_client(self):
        self.is_running = True
        
        while self.is_running:
            is_new_message = True
            while True:

                self.current_message += self.client_socket.recv(self.HEADERSIZE_ENLARGED).decode("utf-8")

                if(is_new_message):
                    self.current_message_len = int(self.current_message[:self.HEADERSIZE])
                    print("new message received length on header:", self.current_message_len)
                    is_new_message = False

              
                print("receiving message:{0}/{1}".format(len(self.current_message) - self.HEADERSIZE, self.current_message_len))


                if(len(self.current_message) - self.HEADERSIZE == self.current_message_len):
                    
                    message_temp = self.current_message[self.HEADERSIZE:]
                    self.messages.append(message_temp)
                    self.current_message = ""

                    is_new_message = True

                    print("full message received")
                    print(message_temp)
                    break

            print(self)


c = client()
c.run_client()


