from tkinter import *
def book():
    windows=Tk()
    windows.title("ONLINE TICKET BOOKING APPLICATION")
    windows.geometry('1366x768')
    windows.configure(bg="LIGHT BLUE")
    lbl1=Label(windows,text="***Enter Journey details***",bg="yellow",font=("Times New Roman",25))
    lbl1.pack()
    lbl2=Label(windows,text="Train no.",font=("Times New Roman",18),bg="Light blue")
    lbl2.place(x=470,y=100)
    ent1=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
    ent1.place(x=570,y=105)
    lbl3=Label(windows,text="Source Stn.",font=("Times New Roman",18),bg="Light blue")
    lbl3.place(x=450,y=150)
    ent2=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
    ent2.place(x=570,y=155)
    lbl4=Label(windows,text="Destination Stn.",font=("Times New Roman",18),bg="Light blue")
    lbl4.place(x=410,y=200)
    ent3=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
    ent3.place(x=570,y=205)
    lbl2=Label(windows,text="Class",font=("Times New Roman",18),bg="Light blue")
    lbl2.place(x=500,y=250)
    ent1=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
    ent1.place(x=570,y=255)
book()