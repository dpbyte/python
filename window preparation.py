from tkinter import *
#from speedtest import Speedtest
import os



def Shutdown():
	return os.system("/shutdown /s /t 1")

#def Download():
#	st=Speedtest()
#	return "value"
	
Mw=Tk()
Mw.title("System Functions")
Mw.geometry("20x20")
#master.configure(bg="light grey")
Mw.configure(bg="red")
Button(Mw,text="Shutdown",command=Shutdown).place(x="20",y="50")
#Button(master,text="Download",command=Download).place(x=10,y=10)
button=Button(Mw,text="Stop",width=15, height=2, command=Mw.destroy)
button.place(x="20",y="80")
button.pack()

Mw.mainloop()