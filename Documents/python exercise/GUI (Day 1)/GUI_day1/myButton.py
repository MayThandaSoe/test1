# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:40:45 2020

@author: Yu Hlaing Win
"""

import tkinter

class MyGUI:
    
    def __init__(self):
        self.window=tkinter.Tk()
        
        #Create Button
        self.my_button=tkinter.Button(self.window,
                                      text='Click Me',
                                      command=self.something)
        
        #Pack the button
        self.my_button.pack()
        
        
        #Enter tkinter mainloop
        tkinter.mainloop()
        
    def something(self):
        #Display message
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking!')
        
my_gui=MyGUI()