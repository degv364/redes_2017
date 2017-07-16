import socket
import sys

#Se crea el socket para la conexion TCP
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12343)
#Este comando establece la conexion
my_socket.connect(server_address)

#Se le solicita al usuario el mensaje a enviar
mensaje = raw_input("Digite mensaje a enviar: ")
print "Envio ", mensaje
#Se envia el mensaje
my_socket.sendall(mensaje)

len_esperado  = len (mensaje)
len_recibido = 0

while len_recibido < len_esperado  :
    #se recibe el mensaje del servidor
    datoServidor = my_socket.recv(1024)
    len_recibido += len(datoServidor)
    print "Dato recibido del servidor ", datoServidor

#Se cierra el socket
my_socket.close()
