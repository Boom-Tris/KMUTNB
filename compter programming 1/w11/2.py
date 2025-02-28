from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)

score1 = StringVar()
score2 = StringVar()
score3 = StringVar()




score1.set("ค่าไฟ")
l1 = Label(frame,textvariable =score1)
l1.place(x=50,y=50)
e1 = Entry(frame,textvariable=score2)
e1.place(x=150,y=50)




l2 =Label(frame,text="ค่าใช้จ่าย")
l2.place(x=50,y=100)




l3 = Label(frame,textvariable =score3)
l3.place(x=200,y=100)




def b():
    if int(score2.get())<=10:
        score3.set(str(int(score2.get())*5))
    elif int(score2.get())<=30:
        score3.set(str((int(score2.get())-10*4.5)+50  ))
    else:
         score3.set(str((int(score2.get())-30*4.0)+140  ))

d = Button(frame,text="CACULATOR",command=b)
d.place(x=100,y=150)


