import time
from tkinter import *
zain=Tk()
zain.geometry("359*150+0+0")
zain.configure(background="sky blue")
zain.resizable(0,0)
zain.overrideredirect(1)
def start():
    current=time.strftime("%H:%M:%S")
    label.config(current=current)
    label.after(200,start)

label=Label(zain,font=("ds-digital",50,"bold"),bg="black",fg="red",bd=50)
label.grid(row=0,column=1)
start()
print('done')
zain.mainloop()