import socket
import sys

#Este comando lo que genera es un modulo de socket de la libreria de python 
#
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12343)
my_socket.connect(server_address)

mensaje = sys.argv[1]
print "Envio ", mensaje
my_socket.sendall(mensaje)

mensajeEsperado  = len (mensaje)
mensajeRecivido = 0

while mensajeRecivido < mensajeEsperado  :
    datoServidor = my_socket.recv(1024)
    mensajeRecivido += len(datoServidor)
    print "Dato recibido del servidor ", datoServidor
    
my_socket.close()
