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
    
    server = server_tcp_socket(args.hostname, args.port)    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
        
    try:
        while True:
            print "Waiting for client connection..."
            csock = server.client_accept()
            try:
                #Wait for client message
                while True:
                    recv_msg = csock.receive()
                    if recv_msg == "STREAM":
                        print "Client requested video streaming"
                        break
                    else:
                        print "Received message from client: ", recv_msg
            except:
                print "Connection closed: Could not receive message from client"
            else:            
                try:
                    #Send Video Streaming
                    while True:
                        ret, frame = cap.read()
                        msg = frame.flatten().tostring()
                        csock.send(msg)
                except:
                    print "Connection closed: Finished video streaming"
                
            csock.close()
    except KeyboardInterrupt:
        print "\nClosing server..."
    finally:
        server.close()
        cap.release()
    

if __name__ == "__main__":
    main()
