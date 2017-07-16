import socket

#Crear el socket de bienvenida, y asignarle direccion
welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12343)
welcome_socket.bind(server_address)

#El socket escucha por peticiones de conexion
welcome_socket.listen(1)
client_data = ''

while True:
    #Al recibir una conexion se crea un nuevo socket llamado
    #connection_socket, que es el qeu establece la conexion entre
    #el servidor y el cliente
    connection_socket, client_address = welcome_socket.accept()
    
    try:
        while client_data != 'fin':
            #se reciben los datos del cliente
            client_data = connection_socket.recv(1024)
	    if client_data:
                #Se retorna el mensaje en mayusculas
	        connection_socket.sendall(client_data.upper())
                print "Enviando dato al cliente: ", client_data.upper()
	    else:
                #En caso de no recibir datos
                print "No mas datos..."
		break
	if (client_data == 'fin'):
		exit(0)
		connection_socket.close()
		
    finally:
        #se cierra la conexion tcp
	connection_socket.close()
	
