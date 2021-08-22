# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:46:28 2020

@author: Yu Hlaing Win
"""

import tkinter

class MyGUI:
    def __init__(self):
        self.window=tkinter.Tk()
        
        #Create click Me button
        self.my_button=tkinter.Button(self.window,
                                      text='Click Me!',
                                      command=self.something)
        
        #Create quit button
        self.quit_button=tkinter.Button(self.window,
                                        text='QUIT',
                                        command=self.window.destroy)
        
        
        #Pack the Click Me button
        self.my_button.pack()
        #Pack the Quit button
        self.quit_button.pack()
        
        #Enter tkinter mainloop
        tkinter.mainloop()
        
    def something(self):
        #Display message
        tkinter.messagebox.showinfo('Response',
                                    'Thanks for clicking!')
        
my_gui=MyGUI()