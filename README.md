# samsung_encrypted_POC
A Proof of concept to pair and send commands to H and J series samsung tvs that use encrypted commmunication.  


Current uses a 3rd party server using the smartview DLLs to figure out the encryption.    

      
         
          
Current Requirements:

* Python3
* websocket-client-py3
* pycrypto

To run just run main   

Once you have paired you may take the session id and key printed from running main, put it in the debug file and then run debug.py to send commands without pairing again
