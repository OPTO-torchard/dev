import sys
import socket
import struct

#host = '10.192.58.10' # SNAP PAC Learning Center
host = '10.192.0.201' # groov EPIC

port = 2001 #MMP default port: 2001
tcode = 5   # read block request
modN = int(sys.argv[1]) # first argument / parameter
chN = int(sys.argv[2])  # second argument / parameter

##create and connect to the socket at host:port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

##Calculate the destination offset:
dest = 0xF01E0000 + (modN * 0x1000) + (chN * 0x40)
#print hex(dest)
#print str(int(str(hex(dest))[2:4], 16)) + ', ' + str(int(str(hex(dest))[4:6], 16)) + ', ' + str(int(str(hex(dest))[6:8], 16)) + ', ' + str(int(str(hex(dest))[8:10], 16))

tc = tcode << 4
##build the block request: 
##      dest  tl_ tc_  src  destoffset..............  len.. exttc
#myBytes = [0, 0,  1, tc, 0, 0, 255, 255, 240, 48, 1, 12, 0, 16, 0, 0];
myBytes = [0, 0, 1, tc, 0, 0, 255, 255, int(str(hex(dest))[2:4],16), int(str(hex(dest))[4:6],16), int(str(hex(dest))[6:8],16), int(str(hex(dest))[8:10],16), 0, 16, 0, 0];

##send the block request and save the response:
nSent = s.send(bytearray(myBytes))
#print '# of bytes sent: ' + str(nSent)
data = s.recv(20)

##upper and lower range of the data block in the package:
up = 20
lo = 16
##confirm block length and print raw data:
#print 'length: ' + str(len(data[lo:up])) + ', raw: ' + data[lo:up]

#Big Endian reordering of the returned bytes:
retBytes = []
for i in range(up-lo):
    retBytes.append(data[up-1-i])
#print the raw and then unpacked bytes:
result = str(struct.unpack_from('i', bytearray(retBytes)))
#print 'length: ' + str(len(retBytes)) + ', raw: ' + str(retBytes)
#print result
print result

#close the socket:
s.close()
