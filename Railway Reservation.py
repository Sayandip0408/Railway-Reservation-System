from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import random
import sqlite3

def new():
    windows=Tk()
    windows.title("Welcome")
    windows.geometry('1366x768')
    windows.configure(bg="white")
    def home():
        windows.destroy()
        login()
    Photo1=PhotoImage(file="C:/Users/suraj/Desktop/Project/icon.png")
    btn1=Button(windows,image=Photo1,text="CLICK",fg="blue",font=("Bell MT",15),bg="white",relief=FLAT,compound=TOP,command=home)
    btn1.place(x=580,y=200)
    windows.mainloop()
    
link="C:/Users/suraj/Desktop/Project/"
conn=sqlite3.connect(link+'RAILWAY.db')

#conn.execute('''CREATE TABLE PASSENGER(FULLNAME VARCHAR(30),AGE INTEGER(3),BERTH VARCHAR(30),NATIONALITY VARCHAR(30),CONTACT_NUMBER INTEGER(12),EMAIL VARCHAR(30));''')
def numden():
    num="1234567890"
    pnr=""
    for i in range(10):
        pnr+=num[random.randint(0,len(num)-1)]
    return pnr

def seat():
    str1="SBA"
    str2="123456789"
    s=""
    for i in range(4):
        s=str1[random.randint(0,len(str1)-1)]+str2[random.randint(0,len(str2)-1,)]
    return s

def combo1():
    cursor=conn.cursor()
    cursor.execute('SELECT SOURCE FROM STATION')
    data=[]
    for row in cursor.fetchall():
        data.append(row[0])
    data1=[]
    for i in data:
        if i not in data1:
            data1.append(i)
    return data1

def combo2():
    #conn=sqlite3.connect('combo.db')
    cursor=conn.cursor()
    cursor.execute('SELECT DESTINATION FROM STATION')
    data=[]
    for row in cursor.fetchall():
        data.append(row[0])
    data1=[]
    for i in data:
        if i not in data1:
            data1.append(i)
    return data1

def welcome(user):
    windows=Tk()
    windows.title("Welcome")
    windows.geometry('1366x768')
    windows.configure(bg="white")
    lbl1=Label(windows, text="RAILWAY TICKET BOOKING",bg="blue",fg="black",font=("Times New Roman bold",30))
    lbl1.pack(side=TOP,fill=X)
    lbl3=Label(windows,text="***NOW YOU CAN USE RAILWAY TICKET BOOKING FACILITY***",bg="yellow",font=("Times New Roman",15))
    lbl3.pack(side=TOP,fill=X)
    photo3=PhotoImage(file="C:/Users/suraj/Desktop/Project/train.gif")
    lbl9=Label(windows,image=photo3)
    lbl9.pack()
    def ticket():
        windows.destroy()
        book(user)

    def pr():
        windows.destroy()
        printt(user)
    def cancel():
        cancelled(user)
    photo=PhotoImage(file="C:/Users/suraj/Desktop/Project/Ticket.gif")
    btn1=Button(windows,image=photo,text="Book Ticket",font=("Times New Roman bold",20),bg="White",relief=FLAT,compound=TOP,command=ticket)
    btn1.place(x=150,y=200)
    photo1=PhotoImage(file="C:/Users/suraj/Desktop/Project/print.gif")
    btn2=Button(windows,image=photo1,text="Print Ticket",font=("Times New Roman bold",20),bg="White",relief=FLAT,compound=TOP,command=pr)
    btn2.place(x=550,y=200)
    photo2=PhotoImage(file="C:/Users/suraj/Desktop/Project/cancel.gif")
    btn3=Button(windows,image=photo2,text="Cancel Ticket",font=("Times New Roman bold",20),bg="White",relief=FLAT,compound=TOP,command=cancel)
    btn3.place(x=950,y=200)
    def back():
        windows.destroy()
        login()
    btn=Button(windows,width=10, text="Log out",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=back)
    btn.place(x=1230,y=100)
    windows.mainloop()


    
def register(): 
    windows=Tk()
    windows.title("Railway Ticket Booking")
    windows.geometry('1366x768')
    lbl=Label(windows, text="RAILWAY TICKET BOOKING",bg="blue",fg="white",font=("Times New Roman bold",30))
    lbl.pack(side=TOP,fill=X)
    photo=PhotoImage(file="C:/Users/suraj/Desktop/Project/train.gif")
    lbl9=Label(windows,image=photo)
    lbl9.pack()
    lbl5=Label(windows,text="Registration Application",font=("Bell MT",25),fg="Black")
    lbl5.place(x=530,y=90)
    lbl1=Label(windows,text="First name",font=("Bell MT",15))
    lbl1.place(x=300,y=220)
    FIRSTNAME=Entry(windows,width=40)
    FIRSTNAME.place(x=420,y=225)
    lbl2=Label(windows,text="Last name",font=("Bell MT",15))
    lbl2.place(x=700,y=220)
    LASTNAME=Entry(windows,width=40)
    LASTNAME.place(x=820,y=225)
    lbl3=Label(windows,text="User name",font=("Bell MT",16))
    lbl3.place(x=300,y=280)
    USERNAME=Entry(windows,width=40)
    USERNAME.place(x=420,y=285)
    lbl4=Label(windows,text="Password",font=("Bell MT",15))
    lbl4.place(x=700,y=280)
    PASSWORD=Entry(windows,width=40,show="*")
    PASSWORD.place(x=820,y=285)
    lbl5=Label(windows,text="Phone Number",font=("Bell MT",15))
    lbl5.place(x=270,y=340)
    PHONE_NO=Entry(windows,width=40)
    PHONE_NO.place(x=420,y=345)
    lbl6=Label(windows,text="Email",font=("Bell MT",15))
    lbl6.place(x=700,y=340)
    EMAIL=Entry(windows,width=40)
    EMAIL.place(x=820,y=345)
    def done():
        val=(FIRSTNAME.get()+" "+LASTNAME.get(),USERNAME.get(),PASSWORD.get(),PHONE_NO.get(),EMAIL.get())
        sql=("INSERT INTO REGISTER (FULL_NAME,USERNAME,PASSWORD,PHONE,EMAIL) VALUES (?,?,?,?,?)");
        conn.execute(sql,val)
        conn.commit()
        windows.destroy()
        login()
    def back():
        windows.destroy()
        login()
    btn=Button(windows,width=20, text="Submit",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=5,relief=SUNKEN,command=done)
    btn.place(x=600,y=420)
    btn=Button(windows,width=10, text="Back",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=back)
    btn.place(x=10,y=60)
    windows.mainloop()

def login():
    windows=Tk()
    windows.title("ONLINE TICKET BOOKING APPLICATION")
    windows.geometry('1366x768')
    windows.configure(bg="LIGHT BLUE")
    lbl1=Label(windows, text="RAILWAY TICKETING SYSTEM",bg="blue",fg="#ffffff",font=("Times New Roman Bold",30))
    lbl1.pack(side=TOP,fill=X)
    lbl2=Label(windows,text="The Online Ticket Booking Portal",bg="blue",fg="White",font=("Times New Roman",20))
    lbl2.pack(side=TOP,fill=X)
    photo=PhotoImage(file="C:/Users/suraj/Desktop/Project/log1.png")
    lbl9=Label(windows,image=photo)
    lbl9.place(x=3,y=1)
    photo3=PhotoImage(file="C:/Users/suraj/Desktop/Project/train.gif")
    lbl9=Label(windows,image=photo3)
    lbl9.pack()
    lbl3=Label(windows,text="***Please, login if you have already registered***",bg="yellow",font=("Times New Roman",15))
    lbl3.place(x=500,y=130)
    lbl4=Label(windows,text="Username",font=("Times New Roman ",15))
    lbl4.place(x=520,y=180)
    ent1=Entry(windows,width=20,borderwidth=3,relief=FLAT)
    ent1.place(x=630,y=180)
    lbl5=Label(windows,text="Password",font=("Times New Roman ",15))
    lbl5.place(x=520,y=210)
    ent2=Entry(windows,width=20,borderwidth=3,relief=FLAT,show="*")
    ent2.place(x=630,y=210)
    lbl6=Label(windows,text="*New User?",bg="red",fg="white",font=("Times New Roman",13),relief=FLAT)
    lbl6.place(x=535,y=295)
    def clicked():
        user=ent1.get()
        cursor=conn.execute("SELECT USERNAME,PASSWORD FROM REGISTER")
        username=[]
        password=[]
        for row in cursor:
            username.append(row[0])
            password.append(row[1])
        indx=0
        if ent1.get() in username:
            indx=username.index(ent1.get())
        user=username[indx]
        passw=password[indx]
        if ent1.get()== user and ent2.get()==passw:
            messagebox.showinfo("Login","Log in Successful..")
            windows.destroy()
            welcome(user)
        else:
            messagebox.showerror("Error","Please insert correct username and password")
    btn=Button(windows,width=15, text="Log in",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=5,relief=GROOVE,command=clicked)
    btn.place(x=630,y=245)
    def clicked1():
        windows.destroy()
        register()
    btn1=Button(windows,width=8, text="Register",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=5,relief=GROOVE,command=clicked1)
    btn1.place(x=630,y=290)
    windows.mainloop()

def book(user):
    windows=Tk()
    windows.title("ONLINE TICKET BOOKING APPLICATION")
    windows.geometry('1366x768')
    windows.configure(bg="LIGHT BLUE")
    lbl1=Label(windows, text="RAILWAY TICKETING SYSTEM",bg="blue",fg="#ffffff",font=("Times New Roman Bold",30))
    lbl1.pack(side=TOP,fill=X)
    lbl2=Label(windows,text="Enter Journey details",bg="blue",fg="White",font=("Times New Roman",20))
    lbl2.pack(side=TOP,fill=X)
    photo1=PhotoImage(file="C:/Users/suraj/Desktop/Project/train.gif")
    lbl3=Label(windows,image=photo1)
    lbl3.pack()
    lbl4=Label(windows,text="Source Stn. : ",font=("Times New Roman",18),bg="Light blue")
    lbl4.place(x=290,y=100)
    cb1=Combobox(windows,width=40)
    cb1['values']=combo1()
    cb1.set("Select")
    cb1.place(x=430,y=105)

     #destination=
    lbl5=Label(windows,text="Destination Stn. : ",font=("Times New Roman",18),bg="Light blue")
    lbl5.place(x=700,y=100)
    cb2=Combobox(windows,width=40)
    cb2['values']=combo2()
    cb2.place(x=880,y=105)
    cb2.set("Select")
    lbl5=Label(windows,text="Date of Journey : ",font=("Times New Roman",18),bg="Light blue")
    lbl5.place(x=470,y=150)
    ent3=Entry(windows,width=30,borderwidth=3,relief=SUNKEN)
    ent3.place(x=660,y=155)
   
    def now():
        lbl2=Label(windows,text="Full name",bg="light blue",font=("Times New Roman",15))
        lbl2.place(x=300,y=390)
        FULLNAME=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        FULLNAME.place(x=450,y=390)
        lbl2=Label(windows,text="Age",bg="light blue",font=("Times New Roman",15))
        lbl2.place(x=300,y=440)
        AGE=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        AGE.place(x=450,y=440)
        lbl4=Label(windows,text="Berth preference",bg="light blue",font=("Times New Roman",15))
        lbl4.place(x=300,y=490)
        BERTH = Combobox(windows,width=30)
        BERTH['values']=("No choice","Lower Berth","Upper Berth","Side Lower Berth","Side Upper Berth") 
        BERTH.current(0)
        BERTH.place(x=450,y=490)
        lbl4=Label(windows,text="Nationality",bg="light blue",font=("Times New Roman",15))
        lbl4.place(x=750,y=390)
        NATIONALITY=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        NATIONALITY.place(x=900,y=390)
        lbl4=Label(windows,text="Contact number",bg="light blue",font=("Times New Roman",15))
        lbl4.place(x=750,y=440)
        CONTACT_NUMBER=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        CONTACT_NUMBER.place(x=900,y=440)
        lbl6=Label(windows,text="Email",bg="light blue",font=("Times New Roman",15))
        lbl6.place(x=750,y=490)
        EMAIL=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        EMAIL.place(x=900,y=490)
        lbl7=Label(windows,text="Username",bg="light blue",font=("Times New Roman",15))
        lbl7.place(x=300,y=540)
        name=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        name.place(x=450,y=540)
        lbl8=Label(windows,text="Debit/Credit Card details",bg="light blue",font=("Times New Roman",15))
        lbl8.place(x=750,y=540)
        card=Entry(windows,width=40,borderwidth=3,relief=SUNKEN)
        card.place(x=965,y=540)
        def submit():
            cursor=conn.execute("SELECT * FROM STATION")
            source=[]
            tr=[]
            trn=[]
            dest=[]
            fare=[]
            for row in cursor:
                source.append(row[0])
                tr.append(row[1])
                trn.append(row[2])
                dest.append(row[3])
                fare.append(row[4])
            if cb1.get() in source:
                indxs=source.index(cb1.get())
            if dest.index(cb2.get())==indxs:
                a=tr[indxs]
                b=trn[indxs]
                c=fare[indxs]
            pnr=numden()
            s=seat()
            val=(FULLNAME.get(),AGE.get(),BERTH.get(),NATIONALITY.get(),CONTACT_NUMBER.get(),EMAIL.get(),name.get(),cb1.get(),cb2.get(),ent3.get(),pnr,a,b,c,s)
            sql=("INSERT INTO PASSENGER (FULLNAME,AGE,BERTH,NATIONALITY,CONTACT_NUMBER,EMAIL,USERNAME,SOURCE,DEST,DATE,PNR,TRAIN,NO,FARE,SEAT) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
            conn.execute(sql,val)
            conn.commit()
            messagebox.showinfo("Payment","Payment Successful")
            windows.destroy()
            printticket(user)
        btn=Button(windows,width=20, text="Make Payment",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=5,relief=SUNKEN,command=submit)
        btn.place(x=560,y=590)
        #windows.destroy()
        #welcome1()
    def back():
        windows.destroy()
        welcome(user)
    def Check():
        cursor=conn.execute("SELECT * FROM STATION")
        source=[]
        tr=[]
        trn=[]
        dest=[]
        fare=[]
        for row in cursor:
            
            source.append(row[0])
            tr.append(row[1])
            trn.append(row[2])
            dest.append(row[3])
            fare.append(row[4])
        if cb1.get() in source:
            indxs=source.index(cb1.get())
        if dest.index(cb2.get())==indxs:
            lbl7=Label(windows,text="                                                                                   ",font=("Times New Roman",18))
            lbl7.place(x=450,y=270)
            lbl8=Label(windows,text="                                                                                   ",font=("Times New Roman",18))
            lbl8.place(x=380,y=270)
            lbl9=Label(windows,text="                                                                                   ",font=("Times New Roman",18))
            lbl9.place(x=600,y=320)
            lbl7.configure(text=tr[indxs])
            lbl8.configure(text=trn[indxs])
            lbl9.configure(text=fare[indxs])
            fare=Label(windows,text="Fare:",font=("Times New Roman",18))
            fare.place(x=550,y=320)
        
            btn=Button(windows,width=10, text="Book now",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=now)
            btn.place(x=720,y=320)
        else:
                messagebox.showerror("Error","No trains found!!!")
        
    
    btn=Button(windows,width=25, text="Find trains",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=Check)
    btn.place(x=550,y=220)
    btn=Button(windows,width=10, text="Back",bg="blue",fg="white",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=back)
    btn.place(x=10,y=110)
    windows.mainloop()



def printticket(user):
    windows=Tk()
    windows.title("ONLINE TICKET BOOKING APPLICATION")
    windows.geometry('1366x768')
    windows.configure(bg="LIGHT BLUE")
    lbl0=Label(windows, text="RAILWAY TICKETING SYSTEM",bg="blue",fg="#ffffff",font=("Times New Roman Bold",30))
    lbl0.pack(side=TOP,fill=X)
    lbl1=Label(windows,text="Print your ticket",bg="blue",fg="White",font=("Times New Roman",20))
    lbl1.pack(side=TOP,fill=X)
    
    #photo1=PhotoImage(file="C:/Users/suraj/Desktop/Project/train.gif")
    #lbl3=Label(windows,image=photo1)
    #lbl3.pack()
    photo=PhotoImage(file="C:/Users/suraj/Desktop/Project/print.png")
    lbl9=Label(windows,image=photo)
    lbl9.pack()
    lb1=Label(windows,text="PNR no.",font=("Times New Roman",17),bg="light blue")
    lb1.place(x=200,y=250)
    pnr=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    pnr.place(x=330,y=250)
    lb2=Label(windows,text="Train no. ",font=("Times New Roman",17),bg="light blue")
    lb2.place(x=200,y=300)
    no=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    no.place(x=330,y=300)
    lb4=Label(windows,text="Date",font=("Times New Roman",17),bg="light blue")
    lb4.place(x=200,y=350)
    date=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    date.place(x=330,y=350)
    lb3=Label(windows,text="From Station",font=("Times New Roman",17),bg="light blue")
    lb3.place(x=200,y=400)
    source=Label(windows,text="                          ",font=("Times New Roman",17),bg="light blue")
    source.place(x=350,y=400)
    lb5=Label(windows,text="Name",font=("Times New Roman",17),bg="light blue")
    lb5.place(x=200,y=450)
    lbl2=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl2.place(x=330,y=450)
    lb6=Label(windows,text="Age",font=("Times New Roman",17),bg="light blue")
    lb6.place(x=200,y=500)
    lbl4=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl4.place(x=330,y=500)
    lb7=Label(windows,text="Email",font=("Times New Roman",17),bg="light blue")
    lb7.place(x=200,y=550)
    lbl8=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl8.place(x=330,y=550)
    lb8=Label(windows,text="Fare",font=("Times New Roman",17),bg="light blue")
    lb8.place(x=700,y=250)
    fare=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    fare.place(x=830,y=250)
    lb9=Label(windows,text="Train name",font=("Times New Roman",17),bg="light blue")
    lb9.place(x=700,y=300)
    train=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    train.place(x=830,y=300)
    lbb=Label(windows,text="Berth",font=("Times New Roman",17),bg="light blue")
    lbb.place(x=700,y=350)
    lbl5=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl5.place(x=830,y=350)
    lbd=Label(windows,text="To Station",font=("Times New Roman",17),bg="light blue")
    lbd.place(x=700,y=400)
    tr=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    tr.place(x=830,y=400)
    lbn=Label(windows,text="Nationality",font=("Times New Roman",17),bg="light blue")
    lbn.place(x=700,y=450)
    lbl6=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl6.place(x=830,y=450)
    lbc=Label(windows,text="Contact no.",font=("Times New Roman",17),bg="light blue")
    lbc.place(x=700,y=500)
    lbl7=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl7.place(x=830,y=500)
    lbs=Label(windows,text="Seat no.",font=("Times New Roman",17),bg="light blue")
    lbs.place(x=700,y=550)
    seat=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    seat.place(x=830,y=550)
     
    cursor=conn.execute("SELECT FULLNAME,AGE,BERTH,NATIONALITY,CONTACT_NUMBER,EMAIL,SOURCE,DEST,DATE,PNR,TRAIN,NO,FARE,SEAT FROM PASSENGER")

    
    for row in cursor:
        lbl2.configure(text=row[0])
        lbl4.configure(text=row[1])
        lbl5.configure(text=row[2])
        lbl6.configure(text=row[3])
        lbl7.configure(text=row[4])
        lbl8.configure(text=row[5])
        source.configure(text=row[6])
        tr.configure(text=row[7])
        date.configure(text=row[8])
        pnr.configure(text=row[9])
        train.configure(text=row[10])
        no.configure(text=row[11])
        fare.configure(text=row[12])
        seat.configure(text=row[13])
    def back():
        windows.destroy()
        book(user)
    btn=Button(windows,width=10, text="Back",bg="white",fg="blue",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=back)
    btn.place(x=10,y=50)
    windows.mainloop()

def printt(user):
    windows=Tk()
    windows.title("ONLINE TICKET BOOKING APPLICATION")
    windows.geometry('1366x768')
    windows.configure(bg="LIGHT BLUE")
    lbl0=Label(windows, text="RAILWAY TICKETING SYSTEM",bg="blue",fg="#ffffff",font=("Times New Roman Bold",30))
    lbl0.pack(side=TOP,fill=X)
    lbl1=Label(windows,text="Print your ticket",bg="blue",fg="White",font=("Times New Roman",20))
    lbl1.pack(side=TOP,fill=X)
    
    #photo1=PhotoImage(file="C:/Users/suraj/Desktop/Project/train.gif")
    #lbl3=Label(windows,image=photo1)
    #lbl3.pack()
    photo=PhotoImage(file="C:/Users/suraj/Desktop/Project/print.png")
    lbl9=Label(windows,image=photo)
    lbl9.pack()
    #name=Entry(windows,width=50,borderwidth=3,relief=FLAT)
    #name.place(x=700,y=10)
    lb1=Label(windows,text="PNR no.",font=("Times New Roman",17),bg="light blue")
    lb1.place(x=200,y=250)
    pnr=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    pnr.place(x=330,y=250)
    lb2=Label(windows,text="Train no. ",font=("Times New Roman",17),bg="light blue")
    lb2.place(x=200,y=300)
    no=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    no.place(x=330,y=300)
    lb4=Label(windows,text="Date",font=("Times New Roman",17),bg="light blue")
    lb4.place(x=200,y=350)
    date=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    date.place(x=330,y=350)
    lb3=Label(windows,text="From Station",font=("Times New Roman",17),bg="light blue")
    lb3.place(x=200,y=400)
    source=Label(windows,text="                          ",font=("Times New Roman",17),bg="light blue")
    source.place(x=350,y=400)
    lb5=Label(windows,text="Name",font=("Times New Roman",17),bg="light blue")
    lb5.place(x=200,y=450)
    lbl2=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl2.place(x=330,y=450)
    lb6=Label(windows,text="Age",font=("Times New Roman",17),bg="light blue")
    lb6.place(x=200,y=500)
    lbl4=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl4.place(x=330,y=500)
    lb7=Label(windows,text="Email",font=("Times New Roman",17),bg="light blue")
    lb7.place(x=200,y=550)
    lbl8=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl8.place(x=330,y=550)
    lb8=Label(windows,text="Fare",font=("Times New Roman",17),bg="light blue")
    lb8.place(x=700,y=250)
    fare=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    fare.place(x=830,y=250)
    lb9=Label(windows,text="Train name",font=("Times New Roman",17),bg="light blue")
    lb9.place(x=700,y=300)
    train=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    train.place(x=830,y=300)
    lbb=Label(windows,text="Berth",font=("Times New Roman",17),bg="light blue")
    lbb.place(x=700,y=350)
    lbl5=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl5.place(x=830,y=350)
    lbd=Label(windows,text="To Station",font=("Times New Roman",17),bg="light blue")
    lbd.place(x=700,y=400)
    tr=Label(windows,text="                  ",font=("Times New Roman",17),bg="light blue")
    tr.place(x=830,y=400)
    lbn=Label(windows,text="Nationality",font=("Times New Roman",17),bg="light blue")
    lbn.place(x=700,y=450)
    lbl6=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl6.place(x=830,y=450)
    lbc=Label(windows,text="Contact no.",font=("Times New Roman",17),bg="light blue")
    lbc.place(x=700,y=500)
    lbl7=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    lbl7.place(x=830,y=500)
    lbs=Label(windows,text="Seat no.",font=("Times New Roman",17),bg="light blue")
    lbs.place(x=700,y=550)
    seat=Label(windows,text="                         ",font=("Times New Roman",17),bg="light blue")
    seat.place(x=830,y=550)
     
   
    cursor=conn.execute("SELECT FULLNAME,AGE,BERTH,NATIONALITY,CONTACT_NUMBER,EMAIL,SOURCE,DEST,DATE,PNR,TRAIN,NO,FARE,SEAT FROM PASSENGER WHERE USERNAME='"+user+"'")
    
    
    for row in cursor:
        lbl2.configure(text=row[0])
        lbl4.configure(text=row[1])
        lbl5.configure(text=row[2])
        lbl6.configure(text=row[3])
        lbl7.configure(text=row[4])
        lbl8.configure(text=row[5])
        source.configure(text=row[6])
        tr.configure(text=row[7])
        date.configure(text=row[8])
        pnr.configure(text=row[9])
        train.configure(text=row[10])
        no.configure(text=row[11])
        fare.configure(text=row[12])
        seat.configure(text=row[13])
    def back():
        windows.destroy()
        welcome(user)
    btn=Button(windows,width=10, text="Back",bg="white",fg="blue",font=("Times New Roman bold",10),borderwidth=3,relief=GROOVE,command=back)
    btn.place(x=10,y=50)
    windows.mainloop()

def cancelled(user):
    delete="DELETE FROM PASSENGER WHERE USERNAME='"+user+"'"
    cursor=conn.execute(delete)
    conn.commit()
    messagebox.showinfo("Cancel","Ticket Cancelled")
new()
