#Proyecto de redes

import socket
import time
from common import *

def main():
    #constants
    udp_ip="127.0.0.1"
    send_port=5006
    recv_port=5005
    message = recv_message(udp_ip, recv_port)
    #time.sleep(1)
    send_message(message.upper(), udp_ip, send_port)

if __name__=="__main__":
    main()
