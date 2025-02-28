from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


q1 = StringVar()
t = Entry(frame,textvariable=q1)
t.pack()

q2 = StringVar()
t2 = Label(frame,textvariable=q2)
t2.pack()

def r1():
    if int(q1.get())>=80:
        q2.set("A")
    elif int(q1.get())>=70:
        q2.set("B")
    elif int(q1.get())>=60:
        q2.set("C")
    elif int(q1.get())>=50:
        q2.set("D")
    else:
          q2.set("F")
    
    
 




d = Button(frame,text="Grade",command=r1)
d.pack()

