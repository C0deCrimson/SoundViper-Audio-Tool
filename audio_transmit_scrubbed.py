#!/usr/bin/env python3
import socket
import sys
import struct
import time
import datetime
import binascii
import os

UDP = ('127.0.0.1', 5005)
Good = bytes.fromhex('<insert audio hex here>')
Good= bytes([int('01000001',2),66]) # will make bytes AB

PDU_H = bytes.fromhex('<hex values go here>')


#print(DATAF)

def sendT(data, UDPT=('127.0.0.1', 3015)):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sent = sock.sendto(data, (UDPT))
	sock.close()

def sendA(data, UDPA=('127.0.0.1', 3015)):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(data, (UDPA))
	sock.close()
def translate_transmission():
        ulaw_audio = os.system("ffmpeg -i " + audio_file + " -codec:a pcM_mulaw audio_input.wav")
def translate_reciever():
        pcm_audio = os.system("ffmpeg -i " + ulaw_audio + " -codec:a pcm_s16le audio_output.wav")

def hex_chunk():
#Set a hard path or create one of each kind of document and choose at use
        inFile = (r'./audio-input.wav')
#read file content and save as hex string (hexCont)
        with open(inFile, 'rb') as f:
	        content = f.read()
#fs, content = wavfile.read(inFile)
        num =0
        #print (len(content))
        #hexCont = (binascii.hexlify(content)) #convert file content to hex
        mod = len(content)%514 
        while(mod != 0):
            content += bytes.fromhex('00')
            mod = len(content)%514
            num += 1
        hexLength = len(content)
        print(num)
        #f=open('./content_check', 'w')
        #print(content, file=f)
        #f.close()
        i = 0 
        step = 514
        content_pieces = [content[i:i+step] for i in range(0, hexLength, step)]
        x = (hexLength/step)
        print(x)
        i = 0
        while (i < x):
#break hexCont into chunks of length "step" and save in hexCont_pieces[x]
            print(i)
            DATA = content_pieces[i]
            DirtyAudio = (PDU_H + DATA)
            sendT(Good)
            sendA(DirtyAudio)
            i += 1
            time.sleep(.01)
#PUT the hex (hexCont_pieces[i]) into the correct place
#Send the message
        print(num)
hex_chunk()
#sendT(Good)
#sendA(Fuzzing)
''' Send hex forward
for hex in range(1,256):
	P_V = bytes.fromhex('{:02x}'.format(hex))
	Fuzzing   = (P_V + X_ID + PDU_T + P_F + TS + PDU_L + PAD_H + S_ID + A_ID + E_ID + R_ID + E_S + TDL_T + S_R + D_L + DATA)
	sendT(Good)
	time.sleep(.01)
	sendA(Fuzzing)
'''
'''
sendT(Good)
start = time.time()
for hex in range(0,65536):
        current = time.time()
        if ((current-start)>=5): #checks to see if 5 seconds has elapsed to resend transmit packet 
                start=current #updates start to new time
                sendT(Good)
        time.sleep(.001) #used to make it so that sender wont clump and eng has time to process (NO DOS)
        S_ID = bytes.fromhex('{:04x}'.format(hex))
        Fuzzing   = (P_V + X_ID + PDU_T + P_F + TS + PDU_L + PAD_H + S_ID + A_ID + E_ID + R_ID + E_S + TDL_T + S_R + D_L + DATA)
        sendT(Good)
        sendA(Fuzzing)

'''
'''  Send hex in reverse
sendT(Good)
start = time.time()
for hex in range(255,0,-1):
	current = time.time()
	if ((current-start)>=5): #checks to see if 5 seconds has elapsed to resend transmit packet 
		start=current #updates start to new time
		sendT(Good)
	time.sleep(.01) #used to make it so that sender wont clump and eng has time to process (NO DOS)
	P_V = bytes.fromhex('{:02x}'.format(hex))
	Fuzzing   = (P_V + X_ID + PDU_T + P_F + TS + PDU_L + PAD_H + S_ID + A_ID + E_ID + R_ID + E_S + TDL_T + S_R + D_L + DATA)
	sendT(Good)
	sendA(Fuzzing)
'''
'''
x=1
sendT(Good)
while (x<=200):
	P_V = bytes.fromhex('06')
	Fuzzing   = (P_V + X_ID + PDU_T + P_F + TS + PDU_L + PAD_H + S_ID + A_ID + E_ID + R_ID + E_S + TDL_T + S_R + D_L + DATA)
	#sendT(Good)
	sendA(Fuzzing)
	x+=1
'''
