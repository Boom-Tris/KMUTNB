from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)

score1 = StringVar()
score2 = StringVar()
score3 = StringVar()
score4 = StringVar()
score5 = StringVar()

fs1 = StringVar()
fs2 = StringVar()
fs3 = StringVar()
fs4 = StringVar()
fs5 = StringVar()
fs6 =StringVar() 
score1.set("คะแนนคนที่1")
l1 = Label(frame,textvariable =score1)
l1.place(x=50,y=50)
e1 = Entry(frame,textvariable=fs1)
e1.place(x=150,y=50)




score2.set("คะแนนคนที่2")
l2 = Label(frame,textvariable =score2)
l2.place(x=50,y=80)
e2 = Entry(frame,textvariable=fs2)
e2.place(x=150,y=80)

score3.set("คะแนนคนที่3")
l3 = Label(frame,textvariable =score3)
l3.place(x=50,y=110)
e3 = Entry(frame,textvariable=fs3)
e3.place(x=150,y=110)

score4.set("คะแนนคนที่4")
l4 = Label(frame,textvariable =score4)
l4.place(x=50,y=140)
e4 = Entry(frame,textvariable=fs4)
e4.place(x=150,y=140)

score5.set("คะแนนคนที่5")
l5 = Label(frame,textvariable =score5)
l5.place(x=50,y=170)
e5 = Entry(frame,textvariable=fs5)
e5.place(x=150,y=170)


l6 = Label(frame,textvariable =fs6)
l6.place(x=200,y=230)

u = Label(frame,text="คะแนนเฉลี่ย / คะแนนมากสุด / คะแนนน้อยสุด")
u.place(x=50,y=190)


def b():
    g = []
    g.append(int(fs1.get()))
    g.append(int(fs2.get()))
    g.append(int(fs3.get()))
    fs6.set(str(sum(g)/len(g))+"/"+str(min(g))+"/"+str(max(g)))
    

d = Button(frame,text="CACULATOR",command=b)
d.place(x=100,y=300)

