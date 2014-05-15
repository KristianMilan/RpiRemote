#IMPORTS#
from subprocess import call
import sys
#IMPORTS#

class CmdParser:
  def __init__(self):
    self.fifoPath = "/home/pi/scripts/tv/omfifo"
  def createFifo(self):
    call("mkfifo " + self.fifoPath, shell=True)
  def removeFifo(self):
    call("rm " + self.fifoPath, shell=True)
  def status(self):
    print "ok"
  def open(self,path):
    call("omxplayer -o hdmi " + path + " " + self.fifoPath +" &", shell=True)
  def play(self):
    call("echo -n p > " + self.fifoPath, shell=True)
  def quit(self):
    call("echo -n q > " + self.fifoPath, shell=True)
