#IMPORTS
import kivy
kivy.require('1.0.5')

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty

from util import Config
from util import RpiConnect
#IMPORTS

class Remote(FloatLayout):
    status_line = ObjectProperty()
    info = StringProperty()

    def __init__(self, **kwargs):
        super(Remote, self).__init__(**kwargs)
        self.conf = Config("config")
        self.conf.parseConfig()
        self.conn = RpiConnect(self.conf.ip,self.conf.port)

    def playButton(self):
        self.status_line.text = "Play clicked"
        self.conn.send("op")

    def quitButton(self):
        self.status_line.text = "Quit clicked"
        self.conn.send("oq")
        exit()

class RemoteApp(App):

    def build(self):
        return Remote()

if __name__ == '__main__':
    RemoteApp().run()
