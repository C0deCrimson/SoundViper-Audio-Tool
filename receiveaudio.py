#!/usr/bin/env python3
import socket
import binascii
import sys

UDP_IP = "127.0.0.1"
UDP_PORT = 3015
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((UDP_IP,UDP_PORT))
goodheader = bytes.fromhex('06011a04')

def translate_transmission():
        #u-law_encoding == F(x) = sgn(x)((ln(1+u|x|)/(ln(1+u)))) -1 <= x <= 1
        #u-law_expansion == F^-1(y)=sgn(y)(1/u)((1+u)^|y|-1) -1<= y <= 1
        ulaw_audio = os.system("ffmpeg -i " + audio_file + " -codec:a pcm_mulaw audio_input.wav")
        
#Send the audio stream
def transmit_audio():
        wave_obj = sa.WaveObject.from_wave_file(ulaw_audio)
        print(Message2)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing

def translate_reciever():
        #pcm_audio = os.system("ffmpeg -i " + ulaw_audio + " -codec:a pcm_s16be audio_output.wav") #This should be pcm_s16le (little endian), I think
        pcm_audio = os.system("ffmpeg -i " + ulaw_audio + " -codec:a pcm_s16le audio_output.wav")


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
