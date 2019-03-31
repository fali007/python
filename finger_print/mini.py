import tkinter as tk
from tkinter import *
import csv
import tkinter.messagebox
import pandas as pd
import webbrowser
from functools import partial

# ...........student reg.............
class register_stu:
	def submit(self):
		roll=self.entry.get()
		name=self.entry0.get()
		print(len(roll),len(name))
		if len(roll)== 0 or len(name)==0:
			tkinter.messagebox.showerror('ALERT', 'Please Enter Name and Roll')
		else:
			print(roll+ " " + name)
			data = open("csv/list_student.csv", "a")
			# writer = csv.writer(data)
			data.write(roll+","+name+","+self.getnum()+"\n")
			data.close()
			print("saved details")

	def getnum(self):
		file=pd.read_csv('csv/list_student.csv')
		file=file['num']
		num=file.loc[file.shape[0]-1]+1
		print(num)
		return(str(num))
			
	def __init__(self):
		print("hi")
		self.reg=Toplevel(m)
		self.reg.title('STUDENT REGISTER')
		self.roll_no = Label(self.reg, text="ROLL NUMBER")
		self.roll_no.pack()
		self.entry = Entry(self.reg)
		self.entry.pack()
		self.entry.focus()

		self.w = Canvas(self.reg, width=400, height=5) 
		self.w.pack()

		self.name = Label(self.reg, text="NAME")
		self.name.pack()
		self.entry0 = Entry(self.reg)
		self.entry0.pack()

		self.w = Canvas(self.reg, width=400, height=5) 
		self.w.pack()
	
		self.button2 =Button(self.reg, text ="SUBMIT",command=self.submit,fg="blue",height=2,width=20)
		self.button2.pack()

		self.w = Canvas(self.reg, width=400, height=5) 
		self.w.pack()

		self.button1 =Button(self.reg, text ="EXIT", command =self.reg.destroy,fg="red",height=2,width=15)
		self.button1.pack()

# ..........faculty registration........
class register_fac:
	def submit(self):
		details=self.entry.get()
		if len(details) == 0:
			tkinter.messagebox.showerror('ALERT', 'Please Enter course name')
		else:
			print(details)
			data = open("csv/list_faculty.csv", "a")
			data.write(details+","+self.getnum()+"\n")
			data.close()
			print("saved details")

	def getnum(self):
		file=pd.read_csv('csv/list_faculty.csv')
		file=file['num']
		num=file.loc[file.shape[0]-1]+1
		print(num)
		return(str(num))

	def __init__(self):
		print("hi")
		self.reg=Toplevel(m)
		self.reg.title('REGISTER FACULTY')
		self.roll_no = Label(self.reg, text="COURSE NAME")
		self.roll_no.pack()
		self.entry = Entry(self.reg)
		self.entry.pack()
		self.entry.focus()

		self.w = Canvas(self.reg, width=400, height=5) 
		self.w.pack()
	
		self.button2 =Button(self.reg, text ="SUBMIT",command=self.submit,fg="blue",height=2,width=20)
		self.button2.pack()

		self.w = Canvas(self.reg, width=400, height=5) 
		self.w.pack()

		self.button1 =Button(self.reg, text ="EXIT", command =self.reg.destroy,fg="red",height=2,width=15)
		self.button1.pack()

class display:
	def disp(self,num):
		print(num)
		name="csv/"+str(num)+".csv"
		df=pd.read_csv(name)
		df.to_html('myTable.htm')
		htmTable=df.to_html()
		new=2
		url="file:///Users/felixgeorge/Desktop/finger_print/myTable.htm"
		webbrowser.open(url,new=new)

	def __init__(self):
		self.win=Toplevel(m)
		self.win.title('COURSES')
		self.data=pd.read_csv('csv/list_faculty.csv')
		self.data=self.data['faculty']
		for i in range(0,self.data.shape[0]):
			self.w = Canvas(self.win, width=400, height=10) 
			self.w.pack()
			self.data.loc[i]=Button(self.win,text=self.data.loc[i].upper(),command=lambda i=i:self.disp(i),height=2,width=25, fg="blue")
			self.data.loc[i].pack()
			self.w = Canvas(self.win, width=400, height=10) 
			self.w.pack()
			name="csv/"+str(i)+".csv"
			file=open(name,"a")
			file.close()
		self.button =Button(self.win, text ="EXIT", command =self.win.destroy,fg="red",height=2,width=15)
		self.button.pack()


# ......display attendance.........
class attendance:
	def __init__(self):
		print("hi")
		self.atte=Toplevel(m)
		self.atte.title('ATTENDANCE')
		self.roll_no = Label(self.atte, text="ENTER ROLL NUMBER")
		self.roll_no.pack()
		self.entry = Entry(self.atte)
		self.entry.pack()
		self.entry.focus()

		self.w = Canvas(self.atte, width=400, height=5) 
		self.w.pack()
	
		self.button2 =Button(self.atte, text ="SUBMIT",command=self.submit,fg="blue",height=2,width=20)
		self.button2.pack()

		self.w = Canvas(self.atte, width=400, height=5) 
		self.w.pack()

		self.button1 =Button(self.atte, text ="EXIT", command =self.atte.destroy,fg="red",height=2,width=15)
		self.button1.pack()

	def submit(self):
		num=self.entry.get()
		if len(num) == 0:
			tkinter.messagebox.showerror('ALERT', 'Please Enter Roll')
		else:
			size=pd.read_csv('csv/list_faculty.csv');
			sub=size['faculty']
			size=size.shape[0]
			att=[0]*(size+1)
			self.shw=Toplevel(m)
			self.shw.title('ATTENDANCE')
			for i in range(0,size):
				temp="csv/"+str(i)+".csv"
				dat=pd.read_csv(temp)
				temp=str(num)
				dat=dat[temp]
				# print(dat)
				for j in range(0,dat.shape[0]):
					att[i]+=dat.loc[j]
				self.wer="%s : %d/%d : %.2f%s"%(sub[i],att[i],sub.shape[0],att[i]/sub.shape[0]*100,"%")
				# print(wer)
				sub[i]=Label(self.shw, text=self.wer.upper())
				sub[i].pack()

# ...............mainn.............
m=Tk()

m.title('ATTENDANCE')

w = Canvas(m, width=400, height=60) 
w.pack() 

button1 = tk.Button(m, text='COURSES',height=2,command=display ,width=25, fg="blue") 
button1.pack()

w = Canvas(m, width=400, height=20) 
w.pack()

button2 = tk.Button(m, text='STUDENT REGISTER', height=2, width=25, command=register_stu, fg="blue") 
button2.pack()

w = Canvas(m, width=400, height=20) 
w.pack()

button3 = tk.Button(m, text='FACULTY REGISTER', height=2, width=25, command=register_fac, fg="blue") 
button3.pack()

w = Canvas(m, width=400, height=20) 
w.pack()

button4 = tk.Button(m, text='SHOW ATTENDANCE', height=2, width=25, command=attendance, fg="blue") 
button4.pack()

w = Canvas(m, width=400, height=25) 
w.pack()

button5 = tk.Button(m, text='QUIT', height=2, width=25, command=m.destroy, fg="red") 
button5.pack()

w = Canvas(m, width=400, height=25) 
w.pack()

m.mainloop()  