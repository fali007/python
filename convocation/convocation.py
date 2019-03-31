import pdf_gen
# import send
from tkinter import *
import tkinter as tk
m=Tk()

m.title('CONVOCATION')

w = Canvas(m, width=400, height=60) 
w.pack() 

button1 = tk.Button(m, text='GENERATE INVITATION CARD',height=2, width=25, command=pdf_gen.pdf_gen(), fg="blue") 
button1.pack()

w = Canvas(m, width=400, height=20) 
w.pack()

button2 = tk.Button(m, text='SEND EMAIL', height=2, width=25, command=m.destroy, fg="blue") 
button2.pack()

w = Canvas(m, width=400, height=20) 
w.pack()

button3 = tk.Button(m, text='QUIT', height=2, width=25, command=m.destroy, fg="red") 
button3.pack()

w = Canvas(m, width=400, height=25) 
w.pack()

m.mainloop()
