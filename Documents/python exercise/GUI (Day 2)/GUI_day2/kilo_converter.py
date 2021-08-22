# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:18:59 2020

@author: Yu Hlaing Win
"""

import tkinter

class KiloConvertor:
    
    #Create main window
    def __init__(self):
        self.main_window =tkinter.Tk()
        
        
        #Create two frames 
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_fram=tkinter.Frame(self.main_window)
        
        #Create lable for the top Frame
        self.kilo_label = tkinter.Label(self.top_frame,
                                        text='Enter distance in kilometer: ')
        self.kilo_entry = tkinter.Entry(self.top_frame,
                                        width=15)
        
        #Pack the label and entry widget
        self.kilo_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        
        #Create the button widget
        self.cal_button=tkinter.Button(self.bottom_fram,
                                       text='Convert',
                                       command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_fram,
                                        text='Quit',
                                        command=self.main_window.destroy)
        
        #Pack the buttons
        self.cal_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #Pack the frames
        self.top_frame.pack()
        self.bottom_fram.pack()
        
        #Enter the mainloop
        tkinter.mainloop()
        
    def convert(self):
        #kilo=float(input('Enter kilometer:'))
        kilo=float(self.kilo_entry.get())
        #convert to miles
        miles=kilo*0.6214
        
        #Display the results
        tkinter.messagebox.showinfo('Results',
                                    str(kilo)+
                                    'kilometers is equal to' +
                                    str(miles)+'miles')
        
        
#Create an instance of kiloConvertor class
kilo_conv=KiloConvertor()        