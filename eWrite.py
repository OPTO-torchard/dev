import sys
import socket
import struct

host = '10.192.0.201' # groov EPIC
port = 2001 #MMP default port: 2001
tcode = 1   # write block request
modN = int(sys.argv[1]) # first argument / parameter
chN = int(sys.argv[2])  # second argument / parameter
val = int(sys.argv[3])  # third argument / parameter

##create and connect to the socket at host:port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

##Calculate the destination offset:
dest = 0xF0220000 + (modN * 0x1000) + (chN * 0x40)

tc = tcode << 4
##build the block request: 
##  [_,_, tlabel_, tc_, src,src, Dest,Dest,   D.4,D.3,D.2,D.1,   len,len, ext.tc,ext.tc]
myBytes = [0, 0, 1, tc, 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0,16,  0,0,  0,0,0,val];

##send the block request and save the response:
nSent = s.send(bytearray(myBytes))
data = s.recv(12)

##upper and lower range of the data block in the package:
up = 8
lo = 4

#Big Endian reordering of the returned bytes:
retBytes = []
for i in range(up-lo):
    retBytes.append(data[up-1-i])
result = str(struct.unpack_from('i', bytearray(retBytes)))
if (int(result[1:-2]) == 0):
    print 'Write success'
else:
    print 'Write failure.'
#close the socket:
s.close()
