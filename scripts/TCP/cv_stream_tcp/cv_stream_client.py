import numpy as np
import cv2
import argparse
from custom_socket_tcp import *


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
                frame = np.fromstring(sock.receive(),dtype=np.uint8).reshape(480,640,3)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except socket.error:
            print "Connection closed: Could not receive streaming"
        except KeyboardInterrupt:
            print "Closing client..."

    cv2.destroyAllWindows()            
    sock.close()
        

if __name__ == "__main__":
    main()
