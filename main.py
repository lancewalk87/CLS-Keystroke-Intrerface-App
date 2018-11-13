'''
* Keystroke Interface
* main.py
* --------------------------------
* Created by Lance T. Walker on 11/12/2018
* Copyright © 2018 CodeLife Productions. All rights reserved.
'''

import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label


# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
class HelloKivy(App):

    # This returns the content we want in the window
    def build(self):
        # Return a label widget with Hello Kivy
        return Label(text="Hello Kivy")


helloKivy = HelloKivy()
helloKivy.run()