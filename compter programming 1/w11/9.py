from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


n1 = IntVar()
n2 = StringVar()
def d():
    
    num = n1.get()
    if(num %2==0):
        n2.set("จำนวนคู่")
    else:
         n2.set("จำนวนคี่")
t = Entry(frame,textvariable=n1)
t.pack()
l = Label(frame,textvariable=n2)
l.pack()

d = Button(frame,text="check",command=d)
d.pack()









    
 





