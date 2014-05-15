#IMPORTS
from socket import *
#IMPORTS

class RpiConnect(object):
  IP = "192.168.1.124" #IP Adress of Rpi
  PORT = 5003 #Port of Rpi
  def __init__(self):
    self.sock = socket(AF_INET, SOCK_STREAM)

  def connect(self):
    self.sock.connect((self.IP,self.PORT))

  def disconnect(self):
    self.sock.close()
  
  def send(self,msg):
    self.sock.send(msg)

