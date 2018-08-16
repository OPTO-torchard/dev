import socket
import sys
import struct
import binascii

host = '10.192.58.10' # SNAP PAC Learning Center
#host = '10.192.0.201' # groov EPIC
port = 2001
#modN = 1
#chN = 22
#tcode = 5 # read block request

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#dest = 0xF01E0000 + (modN * 0x1000) + (chN * 0x40)
#print dest

myBytes = [0, 0, 12, 80, 0, 0, 255, 255, 240, 48, 1, 12, 0, 16, 0, 0];

print '# of bytes sent: ' + str(s.send(bytearray(myBytes)))
data = s.recv(20)
up = 20
lo = 16

print 'length: ' + str(len(data[lo:up]))

print 'raw: ' + data[lo:up]

print 'ISO-8859-1: ' + str(data[lo:up].decode('ISO-8859-1'))

output = []
for i in range(up-lo):
    output.append(data[up-1-i])

print 'length ' + str(len(output)) + ': ' + str(output)

print 'unpack: ' + str(struct.unpack_from('i', bytearray(output)))

print '\n\n\n'

#print struct.unpack('<f', binascii.unhexlify(data.replace('\n','')[1:]))

#print 'encode: ' + data[1:].encode(errors='surrogateescape')

s.close()
