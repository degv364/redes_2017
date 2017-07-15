import socket
import sys

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12343)
my_socket.bind(server_address)
my_socket.listen(1)
client_data = ''

while True:
    connection, client_address = my_socket.accept()
    
    try:
        while client_data != 'fin':
            client_data = connection.recv(1024)
	    if client_data:
	        connection.sendall(client_data.upper())
                print "Enviando dato al cliente: ", client_data.upper()
	    else:
                print "No hay mas datos"
		break
    finally:
	connection.close()

connection.close()
