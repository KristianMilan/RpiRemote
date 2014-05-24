###IMPORTS
from util import RpiListener
from omx import OmxHandler
###IMPORTS

listener = RpiListener()
cp = OmxHandler()
cp.createFifo()
listener.bind()
print "Established listener. Waiting for incoming commands."

continueParsing = True
while continueParsing:
  cmd = listener.listenForCmd()
  continueParsing = cp.parseCmd(cmd)
listener.unbind()
cp.removeFifo()
