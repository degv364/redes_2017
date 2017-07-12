import socket
import sys

#Este comando lo que genera es un modulo de socket de la libreria de python 
#
My_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12343)
My_socket.connect(server_address)

mensaje = sys.argv[1]
print >>sys.stderr, 'envio "%s"'% mensaje
My_socket.sendall(mensaje)

mensajeEsperado  = len (mensaje)
mensajeRecivido = 0

while mensajeRecivido < mensajeEsperado  :
	datoServidor = My_socket.recv(16)
	mensajeRecivido += len(datoServidor)
	print >>sys.stderr, 'dato recivido del servidor "%s"' % datoServidor
	 
My_socket.close()
