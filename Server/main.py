###IMPORTS
from util import RpiListener
from util import DirectoryHandler
from omx import OmxHandler
###IMPORTS

listener = RpiListener()
cp = OmxHandler()
cp.createFifo()
dir = DirectoryHandler("/home/pi") 
listener.bind()
print "Established listener. Waiting for incoming commands."
listener.startListening()

continueParsing = True
while continueParsing:
  print "Listening..."
  cmd = listener.listenForCmd()
  continueParsing = cp.parseCmd(cmd)
print "Stopping listening"
listener.stopListening()
listener.unbind()
cp.removeFifo()
