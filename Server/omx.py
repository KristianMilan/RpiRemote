#IMPORTS#
from subprocess import call
import sys
#IMPORTS#

class OmxHandler:
  def __init__(self):
    self.fifoPath = "/home/pi/omfifo"
  def createFifo(self):
    call("mkfifo " + self.fifoPath, shell=True)
  def removeFifo(self):
    call("rm " + self.fifoPath, shell=True)
  def open(self,path):
    call("omxplayer -o hdmi " + path + " " + self.fifoPath +" &", shell=True)

  def parseCmd(self,cmd):
    if cmd=="op":
      print "Command: play"
      self.__play()
      return True
    elif cmd=="oq":
      print "Command: quit"
      self.__quit()
      return False
    else:
      print "Unknown command"
      return True

  def __play(self):
    call("echo -n p > " + self.fifoPath, shell=True)
  def __quit(self):
    call("echo -n q > " + self.fifoPath, shell=True)
