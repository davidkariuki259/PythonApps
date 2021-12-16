#for program to work, admin priviledges must be provided
#ie- program must be run using admin account/priviledges

import time
from tkinter import *
import tkinter.messagebox
from ctypes import * 

def deactivator(duration):	#function that renders input inactive for the specified amount of time
	ok=windll.user32.BlockInput(True)	#prevent input
	time.sleep(duration)	#deactivate for given duration
	ok=windll.user32.BlockInput(False)	#restore input capability
	tkinter.messagebox.showinfo('Finished','Keyboard says: \"I\'m Baaaack!!!\"!')
	return

	
def submission():	#function that is called upon submission of values
	try:
		hours,minutes,seconds=(0,0,0)	#initialized to zero, in case user does not supply values
		if (hours_entry.get()):	#if entry is not empty, assign supplied value
			h=hours_entry.get()
			hours=int(h)
		if(minutes_entry.get()):
			m=minutes_entry.get()
			minutes=int(m)
		if(seconds_entry.get()):
			s=seconds_entry.get()
			seconds=int(s)	
		total_seconds=(3600*hours)+(60*minutes)+seconds	#total amount of seconds that input will be disabled
		
		answer=tkinter.messagebox.askquestion('ALERT', 'Proceed to deactivate keyboard and mouse for '+str(total_seconds)+' seconds?\n Ensure that the window in focus is the \
correct one before clicking YES as action cannot be undone')	#prompt user to confirm deactivation, this gives opportunity to select correct window that will be in focus during deactivation period
		
		if answer=='yes':
			root.withdraw()	#hide window upon deactivation
			deactivator(total_seconds)
			root.deiconify()
			return
		
		if answer=='no':
			tkinter.messagebox.showinfo("Aborted","Deactivation Aborted")
			return

	except:	#handling invalid input
		tkinter.messagebox.showinfo("Invalid Input!",'Please Enter valid numeric input for hours, minutes and seconds')
		return		



####################tkinter window#########################
root=Tk()
labelfont = ('Courier', 12)	#set font to be used
root.geometry("600x160+300+300")	#set size and position of window
root.title("Input Deactivator")
root.attributes("-topmost", True)

#use frames
topframe=Frame(root)
bottomframe=Frame(root)

#labels and entries
entry_label=Label(topframe, text="Enter the duration in hours, minutes and seconds")
hours_label=Label(bottomframe,text="Hours:")
hours_entry=Entry(bottomframe)
minutes_label=Label(bottomframe,text="Minutes:")
minutes_entry=Entry(bottomframe)
seconds_label=Label(bottomframe,text="Seconds:")
seconds_entry=Entry(bottomframe)
submit_button=Button(bottomframe, text="Enter", command=submission)

#configure font
entry_label.config(font=labelfont)
hours_label.config(font=labelfont)
hours_entry.config(font=labelfont)
minutes_label.config(font=labelfont)
minutes_entry.config(font=labelfont)
seconds_label.config(font=labelfont)
seconds_entry.config(font=labelfont)
submit_button.config(font=labelfont)

#pack frames
topframe.pack()
bottomframe.pack(side=BOTTOM)

#pack buttons into the window
#note that entry_label is in a different frame from the rest of the widgets
entry_label.pack()

#widgets in bottomframe
hours_label.grid(row=1,column=0)
hours_entry.grid(row=1,column=1,pady=3)
minutes_label.grid(row=2,column=0)
minutes_entry.grid(row=2,column=1,pady=3)
seconds_label.grid(row=3,column=0)
seconds_entry.grid(row=3,column=1,pady=3)
submit_button.grid(row=4, pady=10, columnspan=2)	#make button centrally positioned between the two columns



root.mainloop()

#################end of tkinter window##############################