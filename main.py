'''
* Keystroke Interface
* main.py
* --------------------------------
* Created by Lance T. Walker on 11/12/2018
* Copyright © 2018 CodeLife Productions. All rights reserved.
'''

# frameworks
import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Label

# Class: Main
class Main(App):
    global Window
    def build(self):
        self.title = "Keystroke Interface"
        Window.clearcolor = (1, 1, 1, 0)
        Window.size = (1024, 768)
        return Label(text="Keystroke Interface")
Main().run()