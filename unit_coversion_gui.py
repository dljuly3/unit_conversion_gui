#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:07:03 2020

@author: dylanl
"""

import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result_ftc.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

def celsius_to_fahrenheit():
    """Convert the value for Celsius to Fahrenheit and insert the
    result into lbl_result_ctf.
    """
    celsius = ent_temperature_ctf.get()
    fahrenheit = ((9/5) * float(celsius)) + 32.
    lbl_result_ctf["text"] = f"{round(fahrenheit,2)} \N{DEGREE FAHRENHEIT}"
'''
def knots_to_mph():
'''
window = tk.Tk()
window.title("Temperature Converter")

#Frame for F to C
frm_entry = tk.Frame(window)
ent_temperature = tk.Entry(frm_entry,width=10)
ent_temperature.insert(0,"212")
ent_temperature.grid(row=0,column=0,sticky="e")
f_label = tk.Label(frm_entry,text="\N{DEGREE FAHRENHEIT}")
f_label.grid(row=0,column=1,sticky="w")
frm_entry.grid(row=0,column=0,padx=10)

btn_convert = tk.Button(
    master= window,
    text="\N{RIGHTWARDS DOUBLE ARROW}",
    command=fahrenheit_to_celsius
    )
btn_convert.grid(row=0,column=1,padx=10)


lbl_result = tk.Label(window,text="100\N{DEGREE CELSIUS}")
lbl_result.grid(row=0,column=2,padx=10)

#Frame for C to F
frm_entry_ctf = tk.Frame(window)
ent_temperature_ctf = tk.Entry(frm_entry_ctf,width=10)
ent_temperature_ctf.insert(0,"100")
ent_temperature_ctf.grid(row=0,column=0,sticky="e")
f_label_ctf = tk.Label(frm_entry_ctf,text="\N{DEGREE CELSIUS}")
f_label_ctf.grid(row=0,column=1,sticky="w")
frm_entry_ctf.grid(row=1,column=0,padx=10)

btn_convert_ctf = tk.Button(
    master= window,
    text="\N{RIGHTWARDS DOUBLE ARROW}",
    command=celsius_to_fahrenheit
    )
btn_convert_ctf.grid(row=1,column=1,padx=10)


lbl_result_ctf = tk.Label(window,text="212\N{DEGREE FAHRENHEIT}")
lbl_result_ctf.grid(row=1,column=2,padx=10)


window.mainloop()