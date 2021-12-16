#program to display image in tkinter window
from tkinter import *  
from PIL import ImageTk,Image  
 
root = Tk()   
img = ImageTk.PhotoImage(Image.open("path_to_image")) #replace path_to_image with actual path  
w=root.winfo_screenwidth()	#width of screen
h=root.winfo_screenheight()	#height of screen
canvas = Canvas(root,width=w,height=h)  #set canvas size to window size
canvas.pack()
canvas.create_image(w/2, h/2, anchor=CENTER, image=img)	#create centrally-positioned image
root.mainloop() 
