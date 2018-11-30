# This library is depricated. Please use https://github.com/eclair4151/SmartCrypto

# samsung_encrypted_POC
A Proof of concept to pair and send commands to H and J series samsung tvs that use encrypted commmunication.  


Current uses a 3rd party server using the smartview DLLs to figure out the encryption.    

      
         
          
Current Requirements:

* Python3
* websocket-client
* pyCryptodome

To run just run main   

Once you have paired you may take the session id and key printed from running main, put it in the debug file and then run debug.py to send commands without pairing again
<br>
<br>
<br>
Note the the following TV Models are most likely incompatible for one reason or another


J4xxx, J50xx, J51xx, J52xx, J53xx, UNxxJ6200, J6201, J6203, J620D   
H4xxx, H510x, H52xx, H53x3, H5403, H6003, H61x3, H6201, H6203, S9, S9C    
<br>
<br>
Troubleshooting:    
If the script seems to pair but wont send commands put   
print(aesLib.generate_command('KEY_VOLDOWN'))   
in line 46 of debug.py and see what it prints out     
<br>
if it prints out something like this:   
5::/com.samsung.companion:{"name":"callCommon","args":[{"Session_Id":6,"body":"[F,%,�,�,�,x,�,,�, ,2,�,�,�,�,=,�,q,�,�,�,n,�,k,N,�,�,5,�,K,�,p,�,],�,z,V,�,�,�,�,b,�,�,x,�,q,.,",�,�,�,�,�,Y,u,�,:,7,i,�,),w,P,c,m,�,�,X,�,�,�,�,,',R,b,L,R,�,,�,/,�,$,�,,H,�,�,�,�,�,,B,�,Q,�,),�,�,�,A,,},�,�,�,�, ,j,�,n,a,o,�,.,L,�,�,E,�,1,�,�,�,�,�,�,�,,W,�,�,�,?,T,�,|,�,�,{,U,�,-,�,v,�,(,�,,Q,�,�,�,h,,Q,�,�,�,,},8,�,�,�,�,",�,�,�,�,U,
,=]"}]}  
<br>
You are most likley running python2. This script requires python3 as of now
