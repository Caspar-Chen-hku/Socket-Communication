#!/usr/bin/python

import socket
import os.path
import sys

def main(argv):

        # open the target file; get file size
        filesize = os.path.getsize(argv[3])
        if (filesize==0):
                print("No such file!")
                return;
        fstream = open(argv[3],"rb")
        
        # create socket and connect to server
        
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd.connect(("localhost",int(argv[2])))

        # once the connection is set up; print out 
        # the socket address of your local socket

        print("The_connection_with", sockfd.getsockname(), "has_been_established")


        # send file name and file size as one string separate by ':'
        # e.g., socketprogramming.pdf:435678

        msg = argv[3] + ":" + str(filesize)
        sockfd.send(msg.encode("ascii"))

        # receive acknowledge - e.g., "OK"
        okmsg = sockfd.recv(1024).decode("ascii")
        print(okmsg)
                
        # send the file contents

        print("Start sending ...")
        while (filesize>0):
                block = fstream.read(1024)
                blockLen = len(block)
                sockfd.send(block)
                filesize-=blockLen
                
        # close connection
        print("[Completed]")
        fstream.close()
        sockfd.close()


if __name__ == '__main__':
        if len(sys.argv) != 4:
                print("Usage: FTclient.py <Server_addr> <Server_port> <filename>")
                sys.exit(1)
        main(sys.argv)
