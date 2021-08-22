# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:20:02 2020

@author: Yu Hlaing Win
"""

import tkinter

class Info:
    
    #Create main window
    def __init__(self):
        self.main_window =tkinter.Tk()
        
        
        #Create two frames 
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_fram=tkinter.Frame(self.main_window)
        
        #Create lable for the top Frame
        self.name_label = tkinter.Label(self.top_frame,
                                        text='FirstName: ')
        self.name_entry = tkinter.Entry(self.top_frame,
                                        width=15)
        
        #Pack the label and entry widget
        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')
        
        #Create lastName
        self.lastName_label = tkinter.Label(self.top_frame,
                                        text='LastName: ')
        self.lastName_entry = tkinter.Entry(self.top_frame,
                                        width=15)
        
        #Pack the label and entry widget
        self.lastName_label.pack(side='left')
        self.lastName_entry.pack(side='left')
        
        #Create Age
        self.age_label = tkinter.Label(self.top_frame,
                                        text='Age: ')
        self.age_entry = tkinter.Entry(self.top_frame,
                                        width=15)
        
        #Pack the label and entry widget
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')
        
        
        #Create the button widget
        self.ok_button=tkinter.Button(self.bottom_fram,
                                       text='Ok',
                                       command=self.show)
        self.quit_button=tkinter.Button(self.bottom_fram,
                                        text='Quit',
                                        command=self.main_window.destroy)
        
        #Pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        #Pack the frames
        self.top_frame.pack()
        self.bottom_fram.pack()
        
        #Enter the mainloop
        tkinter.mainloop()
        
    def show(self):
        #kilo=float(input('Enter kilometer:'))
        firstName=self.name_entry.get()
        lastName=self.lastName_entry.get()
        age=self.age_entry.get()
        tkinter.messagebox.showinfo('Info','FirstName: '
                                    +firstName+'\n'+
                                    'LastName: '+lastName +
                                    '\n'+ 'Age: '+age)
        
        
#Create an instance of kiloConvertor class
info=Info()    