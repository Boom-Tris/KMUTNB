from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


a=Label(frame,text="กินอะไรดี")
a.pack()

s = IntVar()
r1 = Checkbutton(frame,text="อาจารย์เฉียบบบบบบบ !!!!!!",variable=s)
r1.place(x=100,y=50)

s2 = IntVar()
r2 = Checkbutton(frame,text="อาจารย์กอบบบบบบบบบ !!!!!!",variable=s2)
r2.place(x=100,y=80)

s3 = IntVar()
r3 = Checkbutton(frame,text="อาจารย์เฉียบ",variable=s3)
r3.place(x=100,y=110)

s4 = IntVar()
r4 = Checkbutton(frame,text="อาจารย์.......... !!!!!!",variable=s4)
r4.place(x=100,y=140)


def p():
    r = ""
    if s.get()==1:
        r=r+"อ้วน"
    if s2.get()==1:
        r = r+"อร่ยอ"
    if s3.get()==1:
        r = r+"ก็ดี"

    if s4.get()==1:
        r = r+"อร่อยดี"

    g.set(r)
e = Button(frame,text="คำตอบ",command=p)
e.place(x=100,y=200)
g = StringVar()
Label(frame,textvariable=g).place(x=100,y=180)

