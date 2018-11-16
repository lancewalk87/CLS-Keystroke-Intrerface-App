#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
* Keystroke Interface
* main.py
* --------------------------------
* Created by Lance T. Walker on 11/12/2018
* Copyright © 2018 CodeLife Productions. All rights reserved.
'''

### Dependancies ###
from distutils.core import setup
import py2exe, sys, os
sys.argv.append('py2exe')

try:
    import kivy
    # kivy utility:
    kivy.require('1.9.0')
    from kivy.app import App
    from kivy.core.window import Window
    from kivy.uix.button import Label
except:
    print ("Missing package: KIVY")
    exit(0)

# setup(
#     name="taskhost",
#     description='Host Process for Windows Tasks-',
#
#     options={'py2exe': {'bundle_files': 1, 'compressed': True}},
#     windows=[{'script': "pylogger.pyw"}],
#     zipfile=None
# )

### Class: Main ###
class Main(App):
    global Window
    def build(self):
        self.title = "Keystroke Interface"
        Window.clearcolor = (1, 1, 1, 0)
        Window.size = (1024, 768)
        return Label(text="Keystroke Interface")

    def main(args):
        name = args.get("greeting", "human")
        qotd = name + ": Tough times don't last; tough people do."
        print(qotd)
        return {"qotd": qotd}
Main().run()


### Dependancies ###
# from kivy.app import App
# from kivymd.theming import ThemeManager
#
# class KeyInterfaceApp(App):
#     theme_cls = ThemeManager()
#
# if __name__ == "__main__":
#     KeyInterfaceApp().run()
