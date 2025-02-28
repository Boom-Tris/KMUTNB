from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


q1 = StringVar()
t = Entry(frame,textvariable=q1)
t.pack()

q1.set("5")

def r1():
    L = int(q1.get())+1
    q1.set(L)

def r2():
    L = int(q1.get())-1
    q1.set(L)
    



d = Button(frame,text="+",command=r1)
d.pack()

d2 = Button(frame,text="+",command=r2)
d2.pack()
