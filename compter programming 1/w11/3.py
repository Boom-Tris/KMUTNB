from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


a=Label(frame,text="หลังสอบคอมโปรเสร็จต้องพูดคำว่าอะไร")
a.pack()

s = IntVar()
r1 = Radiobutton(frame,text="อาจารย์เฉียบบบบบบบ !!!!!!",variable=s,value=1)
r1.place(x=100,y=50)

r2 = Radiobutton(frame,text="อาจารย์กอบบบบบบบบบ !!!!!!",variable=s,value=2)
r2.place(x=100,y=80)


r3 = Radiobutton(frame,text="อาจารย์เฉียบ",variable=s,value=3)
r3.place(x=100,y=110)

r4 = Radiobutton(frame,text="อาจารย์.......... !!!!!!",variable=s,value=4)
r4.place(x=100,y=140)


g = StringVar()

def t():
    if s.get() == 1:
        g.set("ถูกต้องแล้วคับ")
    else:
        g.set("ผิด")

d = Button(frame,text="คำตอบ",command=t)
d.place(x=100,y=200)
Label(frame,textvariable=g).place(x=100,y=180)
        
        






   



