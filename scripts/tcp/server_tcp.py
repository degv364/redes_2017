import socket
import sys

My_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12343)
My_socket.bind(server_address)
My_socket.listen(1)
client_data = ''

while True:
	connection, client_address = My_socket.accept()
	
	try:
		while client_data != 'fin':
				client_data = connection.recv(15)
				if client_data:
					
					connection.sendall(client_data.upper())
					print >>sys.stderr, 'Enviando dato al cliente "%s"' % client_data.upper()
				else:
					print >>sys.stderr, 'no hay mas datos', client_address
					break
	finally:
		connection.close()
connection.close()
