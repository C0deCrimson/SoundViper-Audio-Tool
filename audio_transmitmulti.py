#!/usr/bin/env python3
import socket
import sys
import struct
import time
import datetime
import binascii
import os

TRANSMIT = bytes.fromhex('')
PDU_H = bytes.fromhex('')

if len(sys.argv) != 2:                          # if no arguments used prints the following
    print('Usage: python3 audio_transmitmulti.py "Audiofile"')
    print("Tool uses Relative location")
    exit()


def sendM(data, UDPM=('226.1.1.17', 3014)):     # creates a multicast socket requires system to have route
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0.2)
        ttl = struct.pack('b', 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
        sent = sock.sendto(data, UDPM)
        sock.close()

def hex_chunk():                                # opens audio file, if errors prints usage
        try:
            inFile = (r'./'+(sys.argv[1]))
            with open(inFile, 'rb') as f:
	            content = f.read()
        except FileNotFoundError:
            print('Usage: python3 audio_transmitmulti.py "Audiofile"')
            print("Tool uses Relative location")
            exit()
        num =0
        mod = len(content)%514 
        while(mod != 0):                        # adds nops to end of file until correct length
            content += bytes.fromhex('00')
            mod = len(content)%514
            num += 1
        hexLength = len(content)
        time.sleep(0.01)
        #print(num)
        print("Added Padding") 
        i = 0                                   # takes hex and puts into array at length required
        step = 514
        content_pieces = [content[i:i+step] for i in range(0, hexLength, step)]
        x = (hexLength/step)
        return (x, content_pieces)

def send_chunks(num_chunks, passed_list):       # sends the hex in chunks
        i = 0
        print("Sending Audio")
        while (i < num_chunks):
            print("\rProgress: "+str(int((i+1)/num_chunks*100)) + "%", end='', flush=True)
            DATA = passed_list[i]
            DirtyAudio = (PDU_H + DATA)
            #sendM(TRANSMIT)
            sendM(DirtyAudio)
            i += 1
            time.sleep(.01)
        print("\nAudio sent")

def main():
    send_chunks(*hex_chunk())

if __name__ == "__main__":
    main()
