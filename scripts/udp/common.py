#Proyecto redes de computadoras

import socket

def user_get_message():
    inp = raw_input("Digite el mensaje a enviar: ")
    return inp.lower()

def send_message(message="default", ip="127.0.0.1", port=1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print "Mensaje a enviar: "+message
    sock.sendto(message, (ip, port))
    del(sock)

def recv_message(ip="127.0.0.1", port=1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    data, addr = sock.recvfrom(1024) #buffer size is 1024B
    print "Mensaje recibido: "+ str(data)
    del(sock)
    return str(data)


