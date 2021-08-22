# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:39:59 2020

@author: Yu Hlaing Win
"""

import tkinter

#class MyGUI:
#    
#    def __init__(self):
#        window=tkinter.Tk()
#        
#        #Enter tkinter mainloop
#        tkinter.mainloop()
#        
#my_gui=MyGUI()
        
#Using Label

class MyGUI:
    def __init__(self):
        self.window=tkinter.Tk()
        
        #Create label widget containing "Hello!" text
        self.label=tkinter.Label(self.window,
                                 text='Hello World!')
        
        self.label.pack()
        
        #Enter tkinter mainloop
        tkinter.mainloop()
        
my_gui=MyGUI()