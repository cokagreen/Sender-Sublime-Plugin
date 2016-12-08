#! /usr/bin/python
#python 2.6
import socket
import sys
import os


if len(sys.argv) == 2:
        file_size = os.stat(sys.argv[1]).st_size
        fd = open(sys.argv[1])
        buf = fd.read()
        buf = str(file_size).zfill(8) + buf
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 12109
        s.connect((host, port))
        print "Remote:", host, port
        print "File Name:", sys.argv[1]
        print "Data Size:", file_size
        print "Send Data:", buf
        s.send(buf)
        print "Send Total:", len(buf)
        print "Receiving ..."
        buf = s.recv(1024)
        print "Received Data:", buf
        print "Received Total:", len(buf)
        print "Data Size:", int(buf[0:8])
        s.close()
else:
        print "Usage: e file"
