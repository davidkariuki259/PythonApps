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
        self.timer_text=self.canvas.create_text((self.w*0.5*0.7)/6,(self.h*0.7)/2.2,fill="darkblue",font="algerian 65",text="00: 00 :00",anchor=W)  #default text in timer is zero
        self.canvas.after(0,self.stop_watch)    #call function immediately canvas is rendered
        self.loop()
    
    def stop_watch(self):
        
        elapsed_mins=self.seconds//60    #mins from seconds
        elapsed_hrs=elapsed_mins//60      #hours from minutes
        elapsed_secs=self.seconds%60     #seconds must be less than 60
        str_elapsed_hrs=str(elapsed_hrs)
        str_elapsed_mins=str(elapsed_mins)
        str_elapsed_secs=str(elapsed_secs)
        self.canvas.itemconfig(self.timer_text,text="{}:{}:{}".format(str_elapsed_hrs.zfill(2),str_elapsed_mins.zfill(2),str_elapsed_secs.zfill(2)))
        print("elapsed {} seconds".format(self.seconds))
        self.seconds+=1
        self.canvas.after(1000,self.stop_watch) #call function after 1000 milliseconds (1 second)
        '''else:
            self.canvas.itemconfig(self.timer_text,text="elapsed 0 Seconds\n")
            self.canvas.itemconfig(self.timer_text,text="Time is up. Bye",font="algerian 50")
            print('bye')
            return
        '''


timed=timer()
timed.set_time(0,0,0)   #initiate time
timed.draw_watch('white')
      
