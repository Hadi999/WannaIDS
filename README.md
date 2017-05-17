# WannaIDS

##### Manual #####

WannaIDS is like an IDS (a tool for monitoring) agaist many attacks who use 'SMB' protocol vulnerabilities like MS08-67 or MS17-010 .
Many of Malwares use those vulnerabilities for be spread or attack systems without user's interaction (Conficker,WannaCry).
WannaIDS is here for prevent this type of attack .
How it Work ?
It store all IP addresses who send Requests in the 'smb' port (445) for exploiting MS17-010 
or others exploits like MS08-67,who exploit  vulnerabilities in the SMB protocol .
(Be vigilent , The tool don't kick them)
How to run it correctly ?
1.Disable SMB server , if not the tool cannot listen in the port 445
2.Forward port 445 in your modem configuration 
3.(optional) Create a rule in the firewall for the port 445 

############################



#### Usage ####
./wannaids.py  #normal usage
./wannaids.py --log=logfile.log # write results in a logfile

############################
