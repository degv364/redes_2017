import socket
import numpy as np
import struct
import argparse
import cv2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="Server hostname or IP Address")
    parser.add_argument("port", help="Server port to listen for connections",
                        type=int)
    parser.add_argument("-d", "--debug", help="Enable debug messages", action="store_true")
    args = parser.parse_args()

    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)

    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.hostname, args.port))
    print "Listening at", sock.getsockname()

    MAX_SIZE = 65535

    client_addr = None
    
    while True:
        msg, client_addr = sock.recvfrom(MAX_SIZE)
        if msg == "STREAM":
            break
        print "Received from client: ", msg

    
    fmt = struct.Struct('!I')
    SEGMENT_SIZE = 60000
    data_size = SEGMENT_SIZE-fmt.size
    
    try:
        print "Sending video stream to client: ", client_addr
        while True:
            frame_str = cap.read()[1].flatten().tostring()
            frame_len = len(frame_str)
            frame_offset = 0
            while frame_offset < frame_len:
                curr_size = min(data_size, frame_len-frame_offset)
                if args.debug:
                    print "curr_size: ", curr_size
                    print "frame_offset: ", frame_offset
                data = frame_str[frame_offset:frame_offset+curr_size]
                sock.sendto(fmt.pack(frame_offset)+data, client_addr)
                frame_offset += curr_size
                
    except KeyboardInterrupt:
        print "\nClosing server.."
        

    sock.close()
    cap.release()

    
if __name__ == "__main__":
    main()
