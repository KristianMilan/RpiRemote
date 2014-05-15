#IMPORTS
import kivy
from kivy.app import App
from kivy.uix.button import Button
#IMPORTS

kivy.require('1.0.7')

class Remote(App):

    def build(self):
        return Button(text='Play')

if __name__ == '__main__':
    Remote().run()
