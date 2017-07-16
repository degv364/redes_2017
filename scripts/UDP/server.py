#Proyecto de redes de computadoras
#En este archivo se define el servidor UDP
import socket
from datetime import datetime as dt

def recfv_message(sock):
    data, addr = sock.recvfrom(1024) #buffer size is 1024B
    print str(dt.now())+" Mensaje recibido: "+ str(data)
    return str(data)



def main():
    #Como la comunicacion se realiza dentro de la misma
    #computadora se utiliza localhost como direccion IP
    udp_ip="127.0.0.1"

    #Se define el puerto
    port=5005

    #Se crea el socket, y se asocia a la interfaz
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, port))

    #Control de flujo
    continuar = True
    while continuar:
        
        #Se recibe el mensaje
        data, client_addr = sock.recvfrom(1024) #datagrama de 1024
        print str(dt.now())+" Mensaje recibido: "+ data

        #Se modifica el mensaje
        message = data.upper()
        print str(dt.now())+" Mensaje a enviar: "+message

        #se envia el mensaje
        sock.sendto(message, client_addr)

        #Se detiene la ejecucion en caso de ser necesario
        continuar = (data!="fin")

    del(sock)

if __name__=="__main__":
    main()
