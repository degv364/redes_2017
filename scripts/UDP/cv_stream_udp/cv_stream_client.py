import socket
import sys
import numpy as np
from multiprocessing import Pipe, Process
import struct
import argparse
import cv2

def video_plot(frame_pipe):
    frame = None
    try:
        while True:
            if frame_pipe.poll():
                frame_str = frame_pipe.recv_bytes()
                frame = np.fromstring(frame_str,dtype=np.uint8).reshape(480,640,3)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                if frame is not None:
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
    except KeyboardInterrupt:
        print "Closing video display"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hostname", help="Server hostname or IP Address")
    parser.add_argument("port", help="Server port to listen for connections",
                        type=int)
    parser.add_argument("-d", "--debug", help="Enable debug messages", action="store_true")

    args = parser.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect((args.hostname, args.port))
        print "Client socket name is", sock.getsockname()
    except socket.error:
        print "Error: Could not find server"
        sys.exit(1)
        
    try:
        request = ''
        while request != "STREAM":
            request = raw_input('--> ')
            sock.send(request)
    except socket.error:
        print "Error: Could not send datagram"
        sys.exit(1)


    frame_from_server, frame_to_plotter = Pipe(False)
    plot_p = Process(target=video_plot, args=(frame_from_server,))
    plot_p.start()

    MAX_SIZE = 65535
    HEIGHT = 480
    WIDTH = 640
    FRAME_LEN = HEIGHT*WIDTH*3

    
    fmt = struct.Struct('!I')
    frame_str = ""
    frame_offset = 0

    while True:
        try:
            msg = sock.recv(MAX_SIZE)
            recv_frame_offset, = fmt.unpack(msg[0:fmt.size])
            data = msg[fmt.size:]
            
            if frame_offset != recv_frame_offset:
                raise ValueError
            
            frame_str += data
            frame_offset += len(data)
            
            if frame_offset == FRAME_LEN:
                if args.debug: print "SENDING FRAME TO PLOT"
                frame_to_plotter.send_bytes(frame_str)
                frame_str = ""
                frame_offset = 0
                
        except ValueError:
            if args.debug:
                print "Unexpected frame offset: ",
                print "Expected:", frame_offset, ", got:", recv_frame_offset,
                print "Diff =", frame_offset - recv_frame_offset
            frame_str = ""
            frame_offset = 0
            
        except KeyboardInterrupt:
            print "\nClosing client..."
            break

    plot_p.join()
    cv2.destroyAllWindows()
    sock.close()
    
    
if __name__ == "__main__":
    main()
