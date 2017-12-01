# samsung_encrypted_POC
A Proof of concept to pair and send commands to H and J series samsung tvs that use encrypted commmunication.  


Current uses a 3rd party server using the smartview DLLs to figure out the encryption.    

      
         
          
Current Requirements:

* Python3
* websocket-client-py3
* pycrypto

To run just run main   

Once you have paired you may take the session id and key printed from running main, put it in the debug file and then run debug.py to send commands without pairing again
<br>
<br>
<br>
Note the the following TV Models are most likely incompatible for one reason or another


J4xxx, J50xx, J51xx, J52xx, J53xx, UNxxJ6200, J6201, J6203, J620D   
H4xxx, H510x, H52xx, H53x3, H5403, H6003, H61x3, H6201, H6203, S9, S9C
