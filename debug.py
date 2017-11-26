import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from aes_lib import AESCipher
import websocket
import requests
import base64
import json
import time
import websocket
import aes_lib



###
###  Command to decrypt a command already made. just enter the data of the command here without the [,]
###  and the key that was used to encrypt it. you can ignore the session
###
# byte_arr = '253,174,166,34,84,89,17,135,64,215,115,109,115,160,192,171,9,193,192,27,69,2,29,144,176,201,169,211,12,105,157,82,85,120,98,186,230,193,80,6,127,145,168,238,38,195,14,192,219,12,17,220,239,77,57,60,95,236,161,83,102,222,45,19'
# key = '3A9CA32AE06C1BA2CC46B84E11C131D3'
#
#
# aeslib = AESCipher(key, 0)
# final = ""
# for b in byte_arr.split(','):
# 	final += hex(int(b))[2:].zfill(2)
# test = aeslib.decrypt(final).decode('utf-8')
# print(test)









###
###SEND COMMAND USING ENC_KEY AND SESSION PRINTED FROM PAIRING
###

enc_key = '0A698C55ED294A14B7867055CE7D1D60'
session = '4'
key_command = 'KEY_VOLDOWN'

tv_address = '10.0.0.46'


millis = int(round(time.time() * 1000))
step4_url = 'http://' + tv_address + ':8000/socket.io/1/?t=' + str(millis)
websocket_response = requests.get(step4_url)
websocket_url = 'ws://' + tv_address + ':8000/socket.io/1/websocket/' + websocket_response.text.split(':')[0]
print(websocket_url)


aesLib = aes_lib.AESCipher(enc_key, session)
connection = websocket.create_connection(websocket_url)
time.sleep(0.35)
#need sleeps cuz if you send commands to quick it fails
connection.send('1::/com.samsung.companion')
#pairs to this app with this command.
time.sleep(0.35)

connection.send(aesLib.generate_command(key_command))
time.sleep(0.35)

connection.close()
