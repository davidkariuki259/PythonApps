#simple python program offering GUI for sending gmail email from the desktop.
#developed using Python 3.7.3 in a Windows environment

from tkinter import *
import tkinter.messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def mail_send():
	email=str(entry_1)
	send_to_email=str(entry_2)
	subject=str(entry_3)
	message=str(entry_4)
	password=str(entry_5)
	if ((not entry_1.get()) or (not entry_2.get()) or (not entry_3.get()) or (len(entry_4.get("1.0", "end-1c")) == 0) or (not entry_5.get())):
		tkinter.messagebox.showinfo('Error!!', 'Please Ensure that all fields are supplied')
	else:
		try:
			msg=MIMEMultipart()
			msg['From']=email
			msg['To']=send_to_email
			msg['Subject']=subject

			msg.attach(MIMEText(message, 'plain'))

			server=smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			server.login(email, password)
			text=msg.as_string()
			server.sendmail(email, send_to_email, text)
			server.quit()
		
		except:
			tkinter.messagebox.showinfo('Error!!', 'Please Ensure that:\n -correct credentials are supplied \n  -insecure access setting is enabled\n -active internet connection is available')

root=Tk()
root.geometry("600x400")
root.title("Gmail email sender")

label_1=Label(root, text="Enter your Email:")
label_2=Label(root, text="Enter Receiver Email:")
label_3=Label(root, text="Enter subject of Email:")
label_4=Label(root, text="Enter message or body:")
label_5=Label(root, text="Enter your Password: ")
entry_1=Entry(root) #mail input
entry_2=Entry(root) 
entry_3=Entry(root) 
entry_4=Text(root, height=10, width=40) 
entry_5=Entry(root, show="*") #do not display the password
send_button=Button(root, text="Send Email", command=mail_send)



label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E) 
label_3.grid(row=2, sticky=E)
label_4.grid(row=3, sticky=E)
label_5.grid(row=4, sticky=E)
entry_1.grid(row=0, column=1, sticky=W+E, pady=5) 
entry_1.focus()
entry_2.grid(row=1, column=1, sticky=W+E,  pady=5) 
entry_3.grid(row=2, column=1, sticky=W+E,  pady=5)
entry_4.grid(row=3, column=1, sticky=W,  pady=5)
entry_5.grid(row=4, column=1, sticky=W+E,  pady=5)
send_button.grid(row=5, rowspan=2)


	
root.mainloop() #keep window displayed
