import socket
import struct

class server_tcp_socket:
    def __init__ (self, hostname, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((hostname, port))
        self.s.listen(1)

    def client_accept (self):
        client_sock, client_name = self.s.accept()
        print "Connection from client: ", client_name 
        return client_tcp_socket(client_sock)
    
    def close (self):
        self.s.close()
        

class client_tcp_socket:
    def __init__ (self, n_socket=None):
        if n_socket is not None:
            self.s = n_socket
        else:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.len_format = struct.Struct('!I')
        
    def connect (self, hostname, port):
        self.s.connect((hostname, port))
        
    def send (self, message):
        msg_size = self.len_format.pack(len(message))
        self.s.sendall(msg_size+message)
        
    def recv_size (self, size):
        recv_msg = ""
        curr_len = 0
        while curr_len < size:
            chunk = self.s.recv(size-curr_len)
            if chunk == '':
                raise EOFError("Connection closed")
            
            recv_msg += chunk
            curr_len = len(recv_msg)
        return recv_msg
        
    def receive (self):
        msg_len_packed = self.recv_size(self.len_format.size)
        msg_len = self.len_format.unpack(msg_len_packed)[0]
        return self.recv_size(msg_len)

    def close (self):
        self.s.close()
