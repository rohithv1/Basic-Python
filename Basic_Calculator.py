# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:42:17 2019

@author: Rohith.Vemulapally
"""

import tkinter as tk

expression = ""

def press_num(inp):
    global expression
    entry.insert(END, inp)
    expression += inp

def clear_all():
    global expression
    entry.delete(0,END)
    expression = ""
    
def equals():
    global expression
    expression = str(eval(expression))
    entry.delete(0,END)
    entry.insert(0, expression)
    

if __name__ == '__main__':
    calc = tk.Tk()
    calc.title('Calculator App')
    entry = tk.Entry(calc)
    entry.grid(row=0, column=0, columnspan = 6, pady = 3)
    
    button1 = tk.Button(calc, text="1", command=lambda : press_num('1')).grid(row=1, column=0, columnspan=1, pady = 3)
    button2 = tk.Button(calc, text="2", command=lambda : press_num('2')).grid(row=1, column=1, columnspan=1, pady = 3)
    button3 = tk.Button(calc, text="3", command=lambda : press_num('3')).grid(row=1, column=2, columnspan=1, pady = 3)
    button4 = tk.Button(calc, text="4", command=lambda : press_num('4')).grid(row=2, column=0, columnspan=1, pady = 3)
    button5 = tk.Button(calc, text="5", command=lambda : press_num('5')).grid(row=2, column=1, columnspan=1, pady = 3)
    button6 = tk.Button(calc, text="6", command=lambda : press_num('6')).grid(row=2, column=2, columnspan=1, pady = 3)
    button7 = tk.Button(calc, text="7", command=lambda : press_num('7')).grid(row=3, column=0, columnspan=1, pady = 3)
    button8 = tk.Button(calc, text="8", command=lambda : press_num('8')).grid(row=3, column=1, columnspan=1, pady = 3)
    button9 = tk.Button(calc, text="9", command=lambda : press_num('9')).grid(row=3, column=2, columnspan=1, pady = 3)
    button_dot = tk.Button(calc, text=".", command=lambda : press_num('.')).grid(row=4, column=0, columnspan=1, pady = 3)
    button0 = tk.Button(calc, text="9", command=lambda : press_num('0')).grid(row=4, column=1, columnspan=1, pady = 3)
    buttonclr = tk.Button(calc, text="AC", command=lambda : clear_all()).grid(row=4, column=2, columnspan=1, pady = 3)
    buttonequals = tk.Button(calc, text="=", command=lambda : equals()).grid(row=4, column=3, columnspan=1, pady = 3)
    buttonadd = tk.Button(calc, text="+", command=lambda : press_num('+')).grid(row=1, column=3, columnspan=1, pady = 3)
    buttonsub = tk.Button(calc, text="-", command=lambda : press_num('-')).grid(row=2, column=3, columnspan=1, pady = 3)
    buttonmul = tk.Button(calc, text="*", command=lambda : press_num('*')).grid(row=3, column=3, columnspan=1, pady = 3)
    buttondiv = tk.Button(calc, text="/", command=lambda : press_num('/')).grid(row=1, column=4, columnspan=1, pady = 3)
    calc.mainloop()
    