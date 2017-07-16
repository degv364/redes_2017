#Proyecto redes de computadoras
#En este archivo se define el cliente UDP

#Biblioteca del proyecto
from common import *

def main():
    #Como la comunicacion se realiza dentor de la misma
    #computadora se utiliza localhost como direccion IP
    udp_ip="127.0.0.1"
    
    #Se definen los puertos para los sockets
    send_port=5005
    recv_port=5006
    
    #Se recibe el input de usuario
    message = user_get_message()

    #se envia el mensaje
    send_message(message, udp_ip, send_port)

    #se recibe el mensaje
    message = recv_message(udp_ip, recv_port)
    
    
if __name__=="__main__":
    main()
