#!/usr/bin/python

import socket
import sys

def main(argv):
        # set port number
        # default is 32341 if no input argument
        if (len(argv)>1):
                server_port = int(argv[1])
        else:
                server_port = 32341
        
        # create socket and bind
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd.bind(("",server_port))
        
        # listen and accept new connection
        sockfd.listen(5)
        new, who = sockfd.accept()

        # print out peer socket address information
        print(who)
        
        # receive file name, file size; and create the file
        try:
                message1 = new.recv(50)
        except socket.error as err:
                print("Recv error: ", err)

        fstream = open("copied_file.pdf","wb")
        print("opened a new file")

        filename, filesize_str = message1.decode("ascii").split(':')
        filesize=int(filesize_str)

        # send acknowledge - e.g., "OK"
        new.send(b'OK')
        
        # receive the file contents
        print("Start receiving . . .")

        received = 0
        while(received<filesize):
                rmsg = new.recv(1024)
                fstream.write(rmsg)
                received+=len(rmsg)


        # close connection
        print("[Completed]")
        new.close()
        sockfd.close()


if __name__ == '__main__':
        if len(sys.argv) > 2:
                print("Usage: FTserver [<Server_port>]")
                sys.exit(1)
        main(sys.argv)
