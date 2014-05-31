#IMPORTS
import socket
#IMPORTS

class RpiListener:
  PORT = 4002 #Port to listen to
  def __init__(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

  def bind(self):
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Enables rebinding of socket
    self.sock.bind(('',self.PORT))
    self.sock.listen(5)
  
  def startListening(self):
    self.client,self.addr = self.sock.accept() 
    print 'Incomming connection from ', self.addr

  def stopListening(self):
    self.client.close()

  def listenForCmd(self):
    cmd = self.client.recv(128)
    print "Recived "+cmd
    return cmd

  def answer(self,msg):
    self.client.send(msg)
    print "Answering with: "+msg

  def unbind(self):
    self.sock.close()
