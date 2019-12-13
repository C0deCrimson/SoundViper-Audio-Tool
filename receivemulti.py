#!/usr/bin/env python3
import socket
import binascii
import sys
import struct

MCAST_GRP = '227.1.1.17'
MCAST_PORT = 3014
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

goodheader = bytes.fromhex('<insert hex here')

def main(outfile):
    while True:
            data, addr = sock.recvfrom(65536)
            if goodheader in data:
                cut_data = data[30:]
                print(cut_data)
                with open(outfile, 'ab+') as f:
                    f.write(cut_data)
            else:
                continue
try:
    main(sys.argv[1])
except IndexError:
    print ("Supply an output file: python3 receiveaudio.py <outfileName>")
except KeyboardInterrupt:
    sock.close()
    print("Thanks for using our tool!")
