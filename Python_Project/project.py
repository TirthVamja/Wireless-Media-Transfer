import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import time
# import pyautogui
import socket
from tkinter import filedialog
import threading
import os
import sys
# import System
class button:
	flag=0 #only send or receiver can work at a time
	flag2="" #take file name to be sended
	flag3=0  #after connection established only then transfer can be occured
	flag4=0  #terminate the socket
	l_flag=0
def lab1():
	s=ttt.lab
	k=0
	while(ttt.flag3==0):
		if(k==5):
			l_wait.configure(text=ttt.lab)
			# l_wait.BackColor = System.Drawing.Color.Transparent;
			s=ttt.lab
			k=0
		else:
			s=s+'.'
			l_wait.configure(text=s)
			# l_wait.BackColor = System.Drawing.Color.Transparent;
		l_wait.grid()
		l_wait.place(x=314,y=14)
		l_wait.update()
		time.sleep(1)
		k+=1
def lab(tt1,tt2):
	ttt.lab=tt1
	tt=threading.Thread(target=lab1)
	tt.start()
	# l_wait.configure(text=tt1)
	# l_wait.grid()
	# l_wait.place(x=314,y=14)
	# l_wait.update()
	l_host.configure(text=tt2)
	l_host.grid()
	l_host.place(x=450,y=14)
	l_host.update()
def sending():
	s=socket.socket()
	ttt.flag4=1
	port=8085
	ttt.flag3=0
	host=hostname.get()
	s.bind((host,port))
	s.listen(1)
	conn,addr=s.accept()
	l_wait.configure(text="Connected")
	ttt.flag3=1
	ttt.connection=conn
	l_wait.update()
	l_host.grid_forget()
	l_host.update()
	l_hostname.grid_forget()
	l_hostname.update()
	t1=threading.Thread(target=receive_file)
	t1.start()
def send(self):
	if ttt.flag==0:
		ttt.flag=1
		print("b_send is clicked")
		# wifi()
		lab("Waiting for receiver.","Host Name :") #printing the label 
		l_hostname.grid()
		l_hostname.place(x=526,y=14)
		l_hostname.update()
		
		#threading for sending button
		t=threading.Thread(target=sending)
		t.start()
		# l_wait.grid_forget()
		# l_wait.update()
def receive_file():
	while(True):
		if hasattr(ttt, 'connection'):
			try:
				size=int(ttt.connection.recv(10).decode())
				ttt.size=size
				# file_name=input("Enter the file name")
				file_n=ttt.connection.recv(10).decode()
				file_name=ttt.connection.recv(int(file_n)).decode()
				# file_na=file_n.decode()
				# size,file_name=file_na.split('//')
				# print(size)
				print(file_name)
				while(True): 
					if os.path.exists(file_name):  #rename the file with (1)...
						xx=len(file_name)
						xy=file_name.rfind('.')
						if(file_name[xy-1]==')'):
							xxy=file_name.rfind('(')
							if xxy!=-1:    #dj(1)->dj(2)
								number=int(file_name[xxy+1:xy-1])+1
								file=list(file_name[:xxy+1])
								file.append(str(number))
								file.append(').')
								file.append(file_name[xy+1:])
								file_name=''.join(file)
						else:
							file=list(file_name[:xy])
							file.append(' (1).')
							file.append(file_name[xy+1:])
							file_name=''.join(file)
					else:
						f=open(file_name,'wb+')
						# while(True):
						file_receive=ttt.connection.recv(int(size)) #sending the file
						# 	if not file_receive:
						# 		break
						# 	else:
						f.write(file_receive)
						f.close()
						print("COMPLETED TRANSFER")
						break
			except ConnectionResetError:
				ttt.flag3=0
				lab("Waiting for receiver.","Host Name :")
				print("connection is aborted")
				terminate()
				break
			except ConnectionRefusedError:
				terminate()
			except ValueError:
				pass
			except Exception:
				terminate()
		else: break
def receiving():
	s=socket.socket()
	ttt.flag4=1
	ttt.flag3=0
	host=hostname.get()
	port=8085
	s.connect((host,port))
	l_wait.configure(text="Connected")
	ttt.flag3=1
	ttt.connection=s
	l_wait.update()
	l_host.grid_forget()
	l_host.update()
	l_hostname.grid_forget()
	l_hostname.update()
	t1=threading.Thread(target=receive_file)
	t1.start()
	# receive_file()
def receive(self):
	if ttt.flag==0:
		ttt.flag=1
		print("b_receive is clicked")
		# wifi()
		lab("Connecting , Wait.","Enter Host Name :") #printing the label
		e1.configure(fg="blue",bd=3)
		# e1 = tk.Entry(m,textvariable = mystring,fg="blue",bd=3)
		e1.place(x=560,y=14)
		e1.focus()
		# e1.update()
		# e1.bind('<Return>',c)
		# t=threading.Thread(target=receiving)
		# t.start()
# def prog():
# 	ttt.k=0
# 	ttt.q=0
# 	print("QWER")
# 	progress.place(x=292,y=410)
# 	progress.update()
# 	while(True):
# 		if(ttt.k>90 or ttt.q==1):
# 			break
# 		# if(k>50):k=97
# 		progress['value'] = ttt.k
# 		progress.update()
# 		print("ttt.k",ttt.k)
# 		# m.update_idletasks()
# 		time.sleep(0.10)
# 		ttt.k+=10
def trans(self):
	# print(hostname.get())
	if ttt.flag==1 and ttt.flag2!="" and ttt.flag3==1:
		print("b_trans is clicked")
		file_n=ttt.flag2.split('/')
		file_name=file_n[len(file_n)-1]
		size = os.path.getsize(ttt.flag2)
		print(size)
		size=str(size)
		# ttt.size=size
		# ttt.connection.send(str(size).encode())
		print(file_name)
		x=f'{size:<10}'+f'{len(file_name):<10}'+file_name
		# print(x)
		# x=str(size)+'//'+file_name
		ttt.connection.send(x.encode())
		f=open(ttt.flag2,'rb+')
		
		# if(size%1024==0):size=1024
		# else:size=size%1024
		file_contain=f.read()
		# print(file_contain)
		# while(file_contain):
		ttt.connection.send(file_contain)
			# file_contain=f.read(1024)
			# print('1')
		# ttt.connection.send('exit'.encode())
		# ttt.connection.send('exit'.encode())
		# print('exit'.encode())
		f.close()
		ttt.q=1
		print("File trans")
		ttt.flag2=""

	else:
		print("RADHE")
# def wifi():
# 	pyautogui.moveTo(x=1186,y=767,duration=0)
# 	pyautogui.doubleClick(x=1186,y=767)
# 	pyautogui.moveTo(x=1159,y=535,duration=0)
def select_file(self):
	m.file_path=filedialog.askopenfilename(initialdir="C:\\Users\\Dhvanik\\Desktop\\DJ",title="Select file",filetype=(("All files","*.mkv;*.gif;*.avi;*.mp4;*.m4p;*.mp3;*.3gp;*.mpc;*.webm;*.wav;*.wma"),("Video files","*.mkv;*.gif;*.avi;*.mp4;*.m4p"),("Audio file","*.mp3;*.3gp;*.mpc;*.webm;*.wav;*.wma")))
	ttt.flag2=m.file_path
	print(ttt.flag2)
def terminate():
	os._exit(0)
	# sys.exit()
	# pid=os.getpid()
	# os.kill(pid, signal.SIGSTOP)
	if ttt.flag4==1:
		
		# ttt.connection.disconnect()
		# print(ttt.sock)
		# ttt.sock.shutdown(socket.SHUT_RDWR)
		# ttt.sock.close()
		# del ttt.sock
		print('Network aborted')
		ttt.flag=0 
		ttt.flag2="" 	
		ttt.flag3=0  							
		ttt.flag4=0

m=tk.Tk()
m.title('Media Transfer')
m.resizable(0,0)  #remove maximize button


ttt=button() #object of the button class

#backgroung image
image2=Image.open("back.png")
image1=ImageTk.PhotoImage(image2)
w=image1.width()
h=image1.height()
m.geometry('%dx%d' % (w,h))
back_label=tk.Label(m,image=image1)
back_label.place(x=0,y=0,relwidth=1,relheight=1)



#send button
img = ImageTk.PhotoImage(Image.open("send1.png"))
b_send = tk.Label(m, image = img)
b_send.bind('<Button -1>', send)
b_send.configure(bd="0")
b_send.place(x=144,y=279)

#receive button
img2=ImageTk.PhotoImage(Image.open("receive1.png"))
b_receive=tk.Label(m,image=img2)
b_receive.configure(bd="0")
b_receive.place(x=463,y=279)   # b_receive.place(relx=0.663,rely=0.590)
b_receive.bind('<Button -1>',receive)

#transfer button
img3=ImageTk.PhotoImage(Image.open("x.png"))
b_transfer=tk.Label(m,image=img3)
b_transfer.configure(bd="0")
b_transfer.place(relx=0.458,rely=0.630)
b_transfer.bind('<Button -1>',trans)

#waiting label
l_wait=tk.Label(m,fg="blue",bd=3)
l_wait.grid_forget()   #hide the label

#HostName label
l_host=tk.Label(m,fg="blue",bd=3)
l_host.grid_forget()

#Print Host
l_hostname=tk.Label(m,text=socket.gethostname(),fg='red',bd=3)
l_hostname.grid_forget()

#entry of the hostname
hostname=tk.StringVar(m)
def mm(self):
	print(e1.get())
	t=threading.Thread(target=receiving)
	t.start()

e1=tk.Entry(m,textvariable=hostname)
e1.bind('<Return>',mm)
e1.grid_forget()

#select file
img11=ImageTk.PhotoImage(Image.open('button.png'))
b_select=tk.Label(m,image=img11,bd='0')
b_select.place(x=305,y=181)
b_select.bind('<Button-1>',select_file)
# b_select=tk.Button(m,text="Select file",command=select_file)
# b_select.place(x=566,y=94)

#close the socket
# b_terminate=tk.Button(m,text="terminate",command=terminate)
# b_terminate.place(x=566,y=114)
# b_terminate.grid_forget()


#progress bar
# progress = Progressbar(m, orient = 'horizontal', length = 100, mode = 'determinate')
# progress.grid_forget()

#close button
m.protocol("WM_DELETE_WINDOW", terminate)

m.mainloop()