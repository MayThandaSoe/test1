# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:19:16 2020

@author: Yu Hlaing Win
"""

import tkinter

class MyGUI:
    def __init__(self):
        self.window=tkinter.Tk()
        
        #Create two frames
        self.top_frame=tkinter.Frame(self.window)
        self.bottom_frame=tkinter.Frame(self.window)
        
        #Create Labels
        self.label1=tkinter.Label(self.top_frame,
                                  text='Apple')
        self.label2=tkinter.Label(self.top_frame,
                                  text='Orange')
        self.label3=tkinter.Label(self.top_frame,
                                  text='Grape')
        
        #Pack the labels
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')
        
        #Create Label for bottom frame
        self.label4=tkinter.Label(self.bottom_frame,
                                  text='Apple')
        self.label5=tkinter.Label(self.bottom_frame,
                                  text='Orange')
        self.label6=tkinter.Label(self.bottom_frame,
                                  text='Grape')
        
        #Pack the labels
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')
        
        #Pack the the frame
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        
        #Enter tkinter mainloop
        tkinter.mainloop()
        
        
my_gui=MyGUI()