from tkinter import *
root=Tk()
root.geometry('340x585')
root.maxsize(340,585)
root.title('Calculator')
Label(root,text="Calculator",font="lucida 25 bold",pady=10).pack()

def click(event):
    global scvalue
    text=event.widget.cget("text")
    if text=='=':
        try:
            if scvalue.get().isdigit():
                value=int(scvalue.get())
            else:
                value=eval(screen.get())
            scvalue.set(value)
            screen.update()
        except SyntaxError :
            x="Syntax Error"
            scvalue.set(x)
            screen.update()
         
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,width=100,textvar=scvalue,relief='sunken',borderwidth=20,font="lucida 20",bg='azure4')
screen.pack(ipady=10,anchor='s')

f=Frame(root,borderwidth=5,bg='azure4',pady=2)
b=Button(f,text="C",padx=148,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X)
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,borderwidth=5,bg='azure4')
b=Button(f,text="7",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="8",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="9",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="/",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,borderwidth=5,bg='azure4')
b=Button(f,text="4",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="5",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="6",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="*",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,borderwidth=5,bg='azure4')
b=Button(f,text="1",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="2",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="3",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="-",padx=29,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,borderwidth=5,bg='azure4')
b=Button(f,text="0",padx=41,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text=".",padx=40,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
b=Button(f,text="+",padx=41,pady=10,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X,side='left')
b.bind('<Button-1>',click)
f.pack()

f=Frame(root,borderwidth=5,bg='azure4')
b=Button(f,text="=",padx=148,font='lucida 15 bold',borderwidth=5,relief='raised')
b.pack(fill=X)
b.bind('<Button-1>',click)
f.pack()

root.mainloop()
