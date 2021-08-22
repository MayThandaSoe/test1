# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:48:00 2020

@author: Yu Hlaing Win
"""

import tkinter

class KiloConvertor():
    
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        #Create two frames
        self.top_frame= tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        #Create the top frame's widgets
        self.kilo_label=tkinter.Label(self.top_frame,
                                      text='Enter kilometers:')
        self.kilo_entry=tkinter.Entry(self.top_frame,
                                      width=10)
        
        #Pack the frames
        self.kilo_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        #Create the widgets for middle frame
        self.mile_label=tkinter.Label(self.mid_frame,
                                      text='Converted to miles: ')
        
        #need create object for StringVar()
        #to assosiate with an output label
        #Use the set method to store a stirng of blank characters
        self.output= tkinter.StringVar()
        
        #Create out put lavel
        self.miles_output=tkinter.Label(self.mid_frame,
                                        textvariable=self.output)
        
        #Pack the middle frame widges
        self.mile_label.pack(side='left')
        self.miles_output.pack(side='left')
        
        #Create the buttons in bottom frame
        self.cal_button=tkinter.Button(self.bottom_frame,
                                       text='Convert',
                                       command=self.convert)
        
        self.quit_button=tkinter.Button(self.bottom_frame,
                                        text='Quit',
                                        command=self.main_window.destroy)
        
        #Pack the buttons
        self.cal_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        #Enter the mainloop
        tkinter.mainloop()
        
    def convert(self):
        #kilo=float(input('Enter kilometer:'))
        kilo=float(self.kilo_entry.get())
        #convert to miles
        miles=kilo*0.6214
        
        #Display the results
        self.output.set(miles)
        
kilo_convert=KiloConvertor()
        
        