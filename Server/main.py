###IMPORTS
from util import RpiListener
from handlers import CommandHandler
###IMPORTS

listener = RpiListener()
cp = CommandHandler()

listener.bind()
print "Established listener. Waiting for incoming commands."

listener.startListening()
while True:
  print "Listening..."
  cmd = listener.listenForCmd()
  answer = cp.parseCmd(cmd)
  running = listener.answer(answer)
  if answer == "SHUTDOWN":
    break
print "Stopping listening"
listener.stopListening()
listener.unbind()
