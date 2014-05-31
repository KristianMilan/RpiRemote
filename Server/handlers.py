#IMPORTS#
from subprocess import call 
import os,sys
sys.path.append(os.path.abspath('../Common'))
from movies import Movie, MovieDict
import sys
#IMPORTS#
class CommandHandler:
  def __init__(self):
    self.omx = OmxHandler()

  def parseCmd(self,cmd):
    #omx commands
    if cmd=="op":
      print "Command: play"
      self.omx.play()
      return "EXECUTED"

    elif cmd=="oq":
      print "Command: quit"
      self.omx.quit()
      return "SHUTDOWN"

    #no command
    else:
      print "Unknown command"
      return "NOCOMMAND"

class OmxHandler:
  def __init__(self):
    self.fifoPath = "/home/pi/omfifo"
    call("mkfifo " + self.fifoPath, shell=True)

  def open(self,path):
    call("omxplayer -o hdmi " + path + " " + self.fifoPath +" &", shell=True)

  def play(self):
    call("echo -n p > " + self.fifoPath + "&", shell=True)

  def quit(self):
    call("echo -n q > " + self.fifoPath + "&", shell=True)
    call("rm " + self.fifoPath, shell=True) 

class DbHandler:
  pass
