import sys
import socket
import struct
#host = '10.192.58.10' # SNAP PAC Learning Center
#host = '10.192.0.201' # groov EPIC
host = sys.argv[1]

port = 2001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
## build uptime block request:                F0  30  01  0C    <- uptime memory location
## [_,_, tlabel_, tc_, src,src, Dest,Dest,   D.4,D.3,D.2,D.1,   len,len, ext.tc,ext.tc]
myBytes = [0, 0, 1, 80,  0,  0,  255, 255,   240, 48,  1, 12,     0, 16, 0,0]
## send request and save the response
nSent = s.send(bytearray(myBytes))
data = s.recv(20)
up = 20
lo = 16
output = []
## reverse byte order:
for i in range(up-lo):
    output.append(data[up-1-i])
print 'uptime: ' + str(struct.unpack_from('i', bytearray(output)))[1:-2] + 'ms\n'
## close socket:
s.close()
