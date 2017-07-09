#Proyecto de redes de computadoras
#En este archivo se define el servidor UDP

#Biblioteca del proyecto
from common import *

def main():
    #Como la comunicacion se realiza dentor de la misma
    #computadora se utiliza localhost como direccion IP
    udp_ip="127.0.0.1"

    #Se definen los puertos para los sockets
    send_port=5006
    recv_port=5005

    #Se recibe el mensaje
    message = recv_message(udp_ip, recv_port)

    #Se envia el mensaje
    send_message(message.upper(), udp_ip, send_port)

if __name__=="__main__":
    main()
