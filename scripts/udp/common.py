#Proyecto redes de computadoras
#En este archivo se definen alguans funciones utilitarias
#comunes del servidor y el cliente
import socket
from datetime import datetime as dt

'''
Le solicita al usuario un mensaje para ser enviado
Retorna el mensaje escrito por el usuario en minusculas
'''
def user_get_message():
    inp = raw_input("Digite el mensaje a enviar: ")
    return inp.lower()

'''
Se crea un socket para enviar el mensaje a una direccion IP
y un puerto especificos
'''
def send_message(message="default", ip="127.0.0.1", port=1000):
    #Se crea el Socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print str(dt.now())+" Mensaje a enviar: "+message
    #Se envia el mensaje
    sock.sendto(message, (ip, port))
    #Se destruye el socket
    del(sock)

'''
Se crea un socket para recibir un mensaje de una direccion IP
y un puerto especificos
''' 
def recv_message(ip="127.0.0.1", port=1000):
    #Se crea el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Se asocia a IP y puerto determinados
    sock.bind((ip, port))
    #Blockea hasta recibir un mensaje
    data, addr = sock.recvfrom(1024) #buffer size is 1024B
    print str(dt.now())+" Mensaje recibido: "+ str(data)
    #Se destruye el socket
    del(sock)
    #Se retorna el mensaje
    return str(data)


