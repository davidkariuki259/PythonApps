#program to count down time for a given duration

from tkinter import *

class timer:
    def __init__(self):
        self.hours=0
        self.minutes=0
        self.seconds=0 #number of seconds to be counted down
        self.colors=['white','black']   #list for storing colors
        self.root=Tk()
        self.root.geometry()
        self.w=self.root.winfo_screenwidth()
        self.h=self.root.winfo_screenheight()
        self.root.geometry("{}x{}".format(int(self.w*0.5),int(self.h*0.75)))	#set size and position of window
        self.root.resizable(width=False, height=False)  #make the window size fixed
        self.canvas = Canvas(self.root,width=(self.w*0.5*0.7),height=(self.h*0.7),bg='blue')  #set canvas size relative to window size
        self.canvas.pack(anchor=CENTER)  #place canvas in center of window
        
    def set_time(self,hrs,min,sec):
        self.hours=hrs
        self.minutes=min
        self.seconds=sec+(60*min)+(3600*hrs)
        return
    
    def loop(self):
        self.root.mainloop()
    
    def draw_watch(self,col):
        self.canvas.create_arc(self.w/35,self.h/10,self.w/35+100,self.w/35+130,start=40,extent=180,width=10,fill=col) #alarm clock left 'ear'
        self.canvas.create_arc(self.w/35+300,self.h/10,self.w/35+400,self.h/10+100,start=-40,extent=180,width=10,fill=col)    #right ear
        self.canvas.create_oval(self.w/35,self.h/10,self.w/35+400,self.w/35+420,width=10,fill=col)  #draw large circle in center of canvas
        self.timer_text=self.canvas.create_text((self.w*0.5*0.7)/6,(self.h*0.7)/2.2,fill="darkblue",font="algerian 70",text="00: 00 :00",anchor=W)  #default text in timer is zero
        self.canvas.after(0,self.stop_watch)    #call function immediately canvas is rendered
        self.loop()
    
    def stop_watch(self):
        
        remainder=str(self.seconds)
        remain_mins=self.seconds//60    #mins from seconds
        remain_hrs=remain_mins//60      #hours from minutes
        remain_secs=self.seconds%60     #seconds must be less than 60
        self.canvas.itemconfig(self.timer_text,text="{}:{}:{}".format(remain_hrs,remain_mins,remain_secs))
        print("remaining {} seconds".format(self.seconds))
        if self.seconds>0:
            self.seconds-=1
            self.canvas.after(1000,self.stop_watch) #call function after 1000 milliseconds (1 second)
        else:
            self.canvas.itemconfig(self.timer_text,text="Remaining 0 Seconds\n")
            self.canvas.itemconfig(self.timer_text,text="Time is up. Bye",font="algerian 50")
            print('bye')
            return


timed=timer()
timed.set_time(0,1,5)   #count down 0 hours, 1 min and 5 seconds
timed.draw_watch('white') 
      
