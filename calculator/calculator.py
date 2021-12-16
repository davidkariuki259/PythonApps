#simple arithmetic calculator made using Python 3.7

#on the use eval()- eval is not entirely secure, as it could execute any valid python code passed to it. hence, the program
#filters out any alphabetic characters passed into the arguments, and returns error if any is found


from tkinter import *
import tkinter.messagebox


def check():	#check if expression contains alphabet characters, called when calculator's equal sign is pressed
	expr=screen.get("1.0",'end-1c')
	expr=expr.replace('\n','')
	for a in expr:
		if (a.isalpha())==True:
			screen.delete("1.0",'end-1c')
			screen.insert(tkinter.INSERT,'Math Error. Invalid Argument')
			return "Math Error"	
	if (len(expr) == 0):	#if no argument is supplied, set value to zero
		screen.delete("1.0",'end-1c')
		screen.insert(tkinter.INSERT,'0')
		return
	else:
		try:	#evaluate expression if all checks are passed. ie- not empty and does not contain alphabet characters
			ans=eval(expr)
			screen.delete("1.0",'end-1c')
			screen.insert(tkinter.INSERT,ans)
			return ans
		except:		#raise exception if evaluation is not valid
			screen.delete("1.0",'end-1c')
			screen.insert(tkinter.INSERT,'Math Error. Invalid Argument')
			return "Math Error"
	

def check2(event):	#bind this function to return button, which requires a parameter unlike the check() function
	expr=screen.get("1.0",'end-1c')
	expr=expr.replace('\n','')
	for a in expr:
		if (a.isalpha())==True:
			screen.delete("1.0",'end-1c')
			screen.insert(tkinter.INSERT,'Math Error. Invalid Argument')
			return "Math Error"	
	if (len(expr) == 0):
		screen.delete("1.0",'end-1c')
		screen.insert(tkinter.INSERT,'0')
		return
	else:
		try:
			ans=eval(expr)
			screen.delete("1.0",'end-1c')
			screen.insert(tkinter.INSERT,ans)
			return ans
		except:
			screen.delete("1.0",'end-1c')
			screen.insert(tkinter.INSERT,'Math Error. Invalid Argument')
			return "Math Error"

def quit():	#bound to exit button
	root.destroy()

	

def input(pressed_number):	#append pressed calculator button to the screen
	expr=screen.get("1.0",'end-1c')
	expr=expr.replace('\n','')
	expr+=pressed_number
	screen.delete("1.0",'end-1c')
	screen.insert(tkinter.INSERT,expr)
	return



def deleter():	#delete on pressing calculator 'delete' button
	expr=screen.get("1.0",'end-1c')
	expr=expr.replace('\n','')
	if expr=='Math Error. Invalid Argument' or expr in 'Math Error. Invalid Argument':
		screen.delete("1.0",'end-1c')
		screen.insert(tkinter.INSERT,'')
		return
	else:
		expr=expr[:-1]
		screen.delete("1.0",'end-1c')
		screen.insert(tkinter.INSERT,expr)
	return
	
def deleter2(event):	#delete on pressing kryboard 'backspace' button
	expr=screen.get("1.0",'end-1c')
	expr=expr.replace('\n','')
	if expr=='Math Error. Invalid Argument' or expr in 'Math Error. Invalid Argument':
		screen.delete("1.0",'end-1c')
		screen.insert(tkinter.INSERT,'')
		return
	else:
		expr=expr[:-1]
		screen.delete("1.0",'end-1c')
		screen.insert(tkinter.INSERT,expr)
	return
#draw the calculator window
root=Tk()
number_font = ('Courier', 12)	#set font to be used
symbol_font=('Courier',12,'bold')
root.geometry("400x500+400+100")	#set size and position of window
root.title("Calculator")
root.bind("<Return>", check2)# so that evaluation occurs whenever 'return' key is pressed
root.bind("<BackSpace>", deleter2)

topframe=Frame(root,bg='red')	#for screen
lowerframe=Frame(root,bg='blue')	#for buttons


screen=Text(topframe, height=10,width=38,bg='lightgreen')	#input widget that acts as calculator screen

#define calculator buttons
button0=Button(lowerframe,text="0",height=3,width=16,bg="black",fg="white",command=lambda:input('0'))
button1=Button(lowerframe,text="1",height=3,width=7,bg="black",fg="white",command=lambda:input('1'))
button2=Button(lowerframe,text="2",height=3,width=7,bg="black",fg="white",command=lambda:input('2'))
button3=Button(lowerframe,text="3",height=3,width=7,bg="black",fg="white",command=lambda:input('3'))
button4=Button(lowerframe,text="4",height=3,width=7,bg="black",fg="white",command=lambda:input('4'))
button5=Button(lowerframe,text="5",height=3,width=7,bg="black",fg="white",command=lambda:input('5'))
button6=Button(lowerframe,text="6",height=3,width=7,bg="black",fg="white",command=lambda:input('6'))
button7=Button(lowerframe,text="7",height=3,width=7,bg="black",fg="white",command=lambda:input('7'))
button8=Button(lowerframe,text="8",height=3,width=7,bg="black",fg="white",command=lambda:input('8'))
button9=Button(lowerframe,text="9",height=3,width=7,bg="black",fg="white",command=lambda:input('9'))
button_point=Button(lowerframe,text=".",height=3,width=7,bg="gray",fg="black",command=lambda:input('.'))
button_open_bracket=Button(lowerframe,text="(",height=7,width=7,bg="gray",fg="black",command=lambda:input('('))
button_close_bracket=Button(lowerframe,text=")",height=7,width=7,bg="gray",fg="black",command=lambda:input(')'))
button_divide=Button(lowerframe,text=chr(247),height=3,width=7,bg="gray",fg="black",command=lambda:input('/'))
button_multiply=Button(lowerframe,text="x",height=3,width=7,bg="gray",fg="black",command=lambda:input('*'))
button_subtract=Button(lowerframe,text="-",height=3,width=7,bg="gray",fg="black",command=lambda:input('-'))
button_add=Button(lowerframe,text="+",height=3,width=7,bg="gray",fg="black",command=lambda:input('+'))
button_evaluate=Button(lowerframe,text="=",height=7,width=7,bg="gray",fg="black",command=check)
button_delete=Button(lowerframe,text="\u2190",height=7,width=7,bg="gray",fg="black",command=deleter)

button_exit=Button(root,text="Exit",command=quit,height=3,width=7)	#not in lower frame but has root as master
##########
#end of buttons
###########


##################################
#arrange widgets in window

#frame containing screen
topframe.pack()
screen.pack(pady=5)
screen.config(font=symbol_font)
# end of screen

#lower frame with buttons
lowerframe.pack(side=TOP, pady=10)

#arrange buttons in lower frame using grid layout for more control than pack
button9.grid(row=0,column=0,padx=2,pady=2)
button8.grid(row=0,column=1,padx=2,pady=2)
button7.grid(row=0,column=2,padx=2,pady=2)
button4.grid(row=1,column=0,padx=2,pady=2)
button5.grid(row=1,column=1,padx=2,pady=2)
button6.grid(row=1,column=2,padx=2,pady=2)
button1.grid(row=2,column=0,padx=2,pady=2)
button2.grid(row=2,column=1,padx=2,pady=2)
button3.grid(row=2,column=2,padx=2,pady=2)
button0.grid(row=3,column=0,padx=2,pady=2,columnspan=2)
button_point.grid(row=3,column=2,padx=2,pady=2)
button_add.grid(row=0,column=3,padx=2,pady=2)
button_subtract.grid(row=1,column=3,padx=2,pady=2)
button_divide.grid(row=2,column=3,padx=2,pady=2)
button_multiply.grid(row=3,column=3,padx=2,pady=2)
button_open_bracket.grid(row=0,column=5,rowspan=2,padx=2,pady=2)
button_close_bracket.grid(row=2,column=5,rowspan=2,padx=2,pady=2)
button_delete.grid(row=0,column=6,rowspan=2,padx=2,pady=2)
button_evaluate.grid(row=2,column=6,rowspan=2,padx=2,pady=2)
#end of lower frame


#set exit button apart from other buttons
button_exit.pack(pady=5,padx=5)
##############################
#end of arrangement of widgets

root.mainloop()	#make window persistent
