import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 5006)

sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print "Waiting for connection"
    connection, client_address = sock.accept()
    try:

        # Recibir los datos en partes pequenas y retransmitir
        while True:
            data = connection.recv(16)
            print "Received: ", str(data)
            #if there is somethig in data
            if data:
                print "sending data to client"
                connection.sendall(data.upper())
            else:
                print "no more data from client ", str(client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()
