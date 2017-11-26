import websocket
import requests
import base64
import json
import time
import websocket
import aes_lib
import uuid
import codecs
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

external_server = 'https://34.210.190.209:5443'
external_headers = {'Authorization': 'Basic b3JjaGVzdHJhdG9yOnBhc3N3b3Jk', 'Content-Type': 'application/json', 'User-Agent': 'Remotie%202/1 CFNetwork/893.7 Darwin/17.3.0'}

#Change here
tv_address = '10.0.0.46'


### STEP 0 START
device_id = '12345'
step0_pin_url = 'http://' + tv_address + ':8080/ws/apps/CloudPINPage'
requests.post(step0_pin_url,data='pin4')
step0_url = 'http://' + tv_address + ':8080/ws/pairing?step=0&app_id=com.samsung.companion&device_id=12345&type=1'
r = requests.get(step0_url) #we can prob ignore this response
### STEP 0 START


### STEP 1 START
pin = input("Enter TV Pin: ")
payload = {'pin': pin, 'payload': '', 'deviceId': device_id}
r = requests.post(external_server + '/step1', headers=external_headers, data=json.dumps(payload), verify=False)
step1_url = 'http://' + tv_address + ':8080/ws/pairing?step=1&app_id=com.samsung.companion&device_id=12345&type=1'
step1_response = requests.post(step1_url, data=r.text)
#### STEP 1 END


### STEP 2 START
payload = {'pin': pin, 'payload': codecs.decode(step1_response.text, 'unicode_escape'), 'deviceId': device_id}
r = requests.post(external_server + '/step2', data=json.dumps(payload), headers=external_headers, verify=False)
step2_url = 'http://' + tv_address + ':8080/ws/pairing?step=2&app_id=com.samsung.companion&device_id=12345&type=1&request_id=0'
step2_response = requests.post(step2_url, data=r.text)
### STEP 2 END


### STEP 3 START
payload = {'pin': pin, 'payload': codecs.decode(step2_response.text, 'unicode_escape'), 'deviceId': device_id}
r = requests.post(external_server + '/step3', data=json.dumps(payload), headers=external_headers, verify=False)
enc_key = r.json()['session_key']
session = r.json()['session_id']
print('session_key: ' + enc_key)
print('session_id: ' + session)
step3_url = 'http://' + tv_address + ':8080/ws/apps/CloudPINPage/run'
requests.delete(step3_url)
### STEP 3 END


print('waiting for a sec...')
time.sleep(2)


## STEP 4 START   WEBSOCKETS
millis = int(round(time.time() * 1000))
step4_url = 'http://' + tv_address + ':8000/socket.io/1/?t=' + str(millis)
websocket_response = requests.get(step4_url)
websocket_url = 'ws://' + tv_address + ':8000/socket.io/1/websocket/' + websocket_response.text.split(':')[0]


time.sleep(1)
print('sending command!')
aesLib = aes_lib.AESCipher(enc_key, session)
connection = websocket.create_connection(websocket_url)
time.sleep(0.35)
connection.send('1::/com.samsung.companion')
time.sleep(0.35)
r = connection.send(aesLib.generate_command('KEY_VOLDOWN'))
time.sleep(0.35)
connection.close()
print('sent')

## STEP 4 END

