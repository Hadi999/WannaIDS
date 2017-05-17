import socket
import sys
import optparse


"""

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
3.Create a rule in the firewall for the port 445 

############################

#### Usage ####

./wannaids.py  #normal usage
./wannaids.py --log=logfile.log # write results in a logfile

############################

note: you should convert file into exe with py2exe for run it without any python intrepretor


"""





parser = optparse.OptionParser()
parser.add_option("--log","-l",dest="log",help="Logging option")
opt , arg =  parser.parse_args()


logo = """

 _       __                        ________  _____
| |     / /___ _____  ____  ____ _/  _/ __ \/ ___/
| | /| / / __ `/ __ \/ __ \/ __ `// // / / /\__ \ 
| |/ |/ / /_/ / / / / / / / /_/ // // /_/ /___/ / 
|__/|__/\__,_/_/ /_/_/ /_/\__,_/___/_____//____/  
                                                    

                                                Hadi Mene (H4d3s)
                                                @Suspicious Shell Activity
                                                Platform: Windows


A Protection agaist Wannacrypt,who store all IP addresses who 
send Requests in the 'smb' port (445) for exploiting MS17-010 
or others exploits like MS08-67,who exploit  vulnerabilities
in the SMB protocol , read manual for more infos

"""
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = ""
port = 445
                
sock.bind((host,port))        

sock.listen(50)
print(logo)
print("[*]listening in port 445")
print("[*]Waiting for connections")
print("[*]Log file : wannaids.log")
print("")

if opt.log : # log option
   	logy = open((opt.log),"a")
   	logy.write("*** WannaIDS log ****""\r\n")
   	logy.write("")
   	logy.close()

elif not opt.log :
   	logy = open("wannaids.log","a")
   	logy.write("*** WannaIDS log ****""\r\n")
   	logy.write("")
   	logy.close()

while True:
   c, addr = sock.accept()
   lol = ("[*]A potential attacker [{}] send a request in port 445".format(addr[0]))

   print (lol)

   if opt.log : # log option
   		logy = open((opt.log),"a")
   		logy.write(lol+"\r\n")
   		logy.close()

   elif not opt.log :
   		logy = open("wannaids.log","a")
   		logy.write(lol+"\r\n")
   		logy.close()

   c.close() 

