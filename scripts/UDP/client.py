#Proyecto redes de computadoras
#En este archivo se define el cliente UDP
import socket
from datetime import datetime as dt


'''
Le solicita al usuario un mensaje para ser enviado
Retorna el mensaje escrito por el usuario en minusculas
'''
def user_get_message():
    inp = raw_input("Digite el mensaje a enviar: ")
    return inp.lower()


def main():
    #Como la comunicacion se realiza dentro de la misma
    #computadora se utiliza localhost como direccion IP
    udp_ip="127.0.0.1"
    
    #Se define el puerto del servidor
    port=5005

    #se crea el socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    continuar = True
    while continuar:
        #Se recibe el input de usuario
        message = user_get_message()
        
        #se envia el mensaje
        print str(dt.now())+" Mensaje a enviar: "+message
        sock.sendto(message, (udp_ip, port))
    
        #se recibe el mensaje
        data, addr = sock.recvfrom(1024)
        print str(dt.now())+" Mensaje recibido: "+ data

        #Se detiene la ejecucion en caso de ser necesario
        continuar = (message!="fin")

    del(sock)
    
if __name__=="__main__":
    main()
