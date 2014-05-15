###IMPORTS
from util import RpiListener
from omx import CmdParser
###IMPORTS

listener = RpiListener()
cp = CmdParser()
cp.createFifo()
listener.bind()
print "Established listener. Waiting for incoming commands."

we = True
while we:
  cmd = listener.listenForCmd()
  if cmd:
    print "Received command: " + cmd
    if cmd == "p":
      # cp.play()
      pass
    if cmd == "q":
      we = False

listener.unbind()
cp.removeFifo()
