from multiprocessing import Process
import os
import time

def exec_client():
    print "Digite el mensaje que debe enviar el cliente:"
    os.system('python2 client.py >> client.out')

def exec_server():
    os.system('python2 server.py >> server.out')

def main():
    server = Process(target=exec_server)
    client = Process(target=exec_client)

    server.start()
    time.sleep(2)
    client.start()

    server.join()
    client.join()

if __name__=="__main__":
    main()
