


import socket
import sys
import ssl 

# help class to represent STOMP messages
class StompMessage:

    def __init__(self,s):

        self.type = ''
        self.headers = []
        self.body = ''

        while self.type == '':
            self.type=self.readline(s).strip()
            
            # note - if an empty line is received, this is a heartbeat
            # print("HEARTBEAT")

        line = self.readline(s).strip()

        while not line == '':
            self.headers.append(line)
            line = self.readline(s).strip()

        byte = s.recv(1)

        while not byte[0] == 0:
            self.body+=byte.decode("UTF-8")
            byte = s.recv(1)




    # TODO - probably needs better charset handling
    @staticmethod
    def readline(s):
        request_line = ""
        while not request_line.endswith('\n'):
            byte = s.recv(1)
            request_line += byte.decode("UTF-8")

        return request_line


class StompConnection:

    def __init__(self, host, port, access_token):
        context = ssl.create_default_context()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host,port))

        self.sock = context.wrap_socket(self.sock, server_hostname=host)

        #send CONNECT message to start session
        self.sock.send(("""CONNECT
passcode:{access_token}
heart-beat: 0,30000

""".format(access_token=access_token) + chr(0)).encode("utf-8"))

        self.connectResponse = self.recv_message()

        if self.connectResponse.type == "CONNECTED":

            #send SUBSCRIBE method to receive content
            self.sock.send(("""SUBSCRIBE
destination:/topic/observations

""" + chr(0)).encode("utf-8"))


    def recv_message(self):
        return StompMessage(self.sock)


