# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:07:00 2017

@author: omerf
"""
import tkinter

root = tkinter.Tk()


w = tkinter.Canvas(root, width=500, height=300, bd = 10, bg = 'white')
w.grid(row = 0, column = 0, columnspan = 2)

b = tkinter.Button(width = 10, height = 2, text = 'Button1')
b.grid(row = 1, column = 0)
b2 = tkinter.Button(width = 10, height = 2, text = 'Button2')
b2.grid(row = 1,column = 1)

root.mainloop()
