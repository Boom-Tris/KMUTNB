from tkinter import*
frame = Tk()
frame.title("Frame")
frame.minsize(500,500)
frame.maxsize(500,500)


q1 = StringVar()
q1.set("O")


d = Button(frame,textvariable=q1,height=10,width=30)
d.pack()


num = 0


def r1():
    global num
    num=num+1
    if num%2==0:
        q1.set('O')
    else:
        q1.set("X")
   
d1 = Button(frame,text="+",command=r1,height=10,width=30)
d1.pack()

    









    
 





