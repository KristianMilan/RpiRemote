#IMPORTS
import kivy
from kivy.app import App
from kivy.uix.button import Button

from util import Config
from util import RpiConnect
#IMPORTS

kivy.require('1.0.7')

class Remote(App):

    def build(self):
        return Button(text='Play')

if __name__ == '__main__':
    conf = Config("config")
    conf.parseConfig()
    conn = RpiConnect(conf.ip,conf.port)
    Remote().run()
