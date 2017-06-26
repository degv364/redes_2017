#Proyecto redes de computadoras

import socket
import time
from common import *

def main():
    #constants
    udp_ip="127.0.0.1"
    send_port=5005
    recv_port=5006
    message = user_get_message()
    send_message(message, udp_ip, send_port)
    #time.sleep(0.2)
    message = recv_message(udp_ip, recv_port)
    
    
if __name__=="__main__":
    main()
