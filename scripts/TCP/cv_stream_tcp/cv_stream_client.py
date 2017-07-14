import numpy as np
import cv2
import pickle
import argparse
from socket_custom import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="Server hostname or IP Address")
    parser.add_argument("port", help="Server port to listen for connections",
                        type=int)
    args = parser.parse_args()
    
    try:
        sock = client_tcp_socket()
        sock.connect(args.hostname, args.port)
        request = ''
        while request != "STREAM":
            request = raw_input('--> ')
            sock.send(request)
        
    except:
        print "Connection closed: Could not send message"
    else:
        try:
            while True: #Get Video Streaming
                frame = pickle.loads(sock.receive())
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except:
            print "Connection closed: Could not receive streaming"
                
        sock.close()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
