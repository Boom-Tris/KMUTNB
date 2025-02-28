from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


q1 = StringVar()
t = Entry(frame,textvariable=q1)
t.pack()

q2 = StringVar()
t2 = Entry(frame,textvariable=q2)
t2.pack()



q3 = StringVar()
t3 = Label(frame,textvariable=q3)
t3.pack()


def r1():
    f = int (q1.get())-int(q2.get())
    q3.set(f)
d1 = Button(frame,text="-",command=r1)
d1.pack()

    



def r2():
    f = int (q1.get())+int(q2.get())
    q3.set(f)
d2 = Button(frame,text="+",command=r2)
d2.pack()




def r3():
    f = int (q1.get())*int(q2.get())
    q3.set(f)
d3 = Button(frame,text="*",command=r3)
d3.pack()




    
 





