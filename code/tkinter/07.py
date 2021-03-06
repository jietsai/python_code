#!/usr/bin/env python3
import time
import tkinter as tk
from threading import Thread


vv = {}
vv["system_run"] = True


def myloop():
    count = 0
    while(True):
        time.sleep(1)
        if(vv['system_run']):
            count += 1
            vv['label02'].config(text="%d" % count)


def stop_count():
    if(vv["system_run"]):
        vv["system_run"] = False 
        vv['btn01'].config(text="RUN")
    else:
        vv["system_run"] = True
        vv['btn01'].config(text="STOP")



def enter_handler(event):
    vv['label01'].config(text = "World")

def leave_handler(event):
    vv['label01'].config(text = "Hello")

def entry_handler(event):
    msg = vv['entry01'].get()
    vv['entry01'].delete(0,tk.END)
    vv['label01'].config(text=msg)

if __name__=="__main__":
    root = tk.Tk()

    label01 = tk.Label(master=root, text = "Hello", font=("Times",36) )
    label01.grid(row=0,column=0)
    ## EVENT ADD
    vv['label01'] = label01
    label01.bind("<Enter>", enter_handler)
    label01.bind("<Leave>", leave_handler)

    label02  = tk.Label(master=root, text= "0", width=5, font=("Times",36))
    label02.grid(row=0,column=1)
    vv['label02'] = label02
    th = Thread(target=myloop)
    th.start()

    btn01 = tk.Button(master=root,text="STOP",font=("Time",36), command=stop_count)
    btn01.grid(row=2,column=0)
    vv['btn01'] = btn01

    entry01 = tk.Entry(master=root,font=("Time",36))
    entry01.bind("<Return>",entry_handler)
    entry01.grid(row=3,column=0,rowspan=2,columnspan=3)
    vv['entry01'] = entry01

    root.mainloop()
