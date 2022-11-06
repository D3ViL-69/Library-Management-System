from tkinter import*
import sqlite3
import time
from datetime import date
import tkinter.messagebox
import random
import os
root=Tk()
root.title('Library Management System')
root.maxsize(1150,600)
root.minsize(1150,600) 
#====================================================
def iExit ():
    root.destroy()
    return
def insertData():
    mem=Tk()
    mem.title('Library Management System')
    mem.maxsize(1000,500)
    mem.configure(bg='Powder Blue')
    member=Frame(mem,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    a=StringVar()
    b=StringVar()
    c=StringVar()
    d=StringVar()
    e=StringVar()
    g=StringVar()
    f=StringVar()
    a.set(random.randint(1000,9999))
    b.set('')
    c.set('')
    d.set('')
    e.set('')
    f.set('')
    g.set(time.strftime('%d/%m/%y'))
    def exite():
        mem.destroy()
    def reset():
        a.set(random.randint(1000,9999))
        b.set('')
        c.set('')
        d.set('')
        e.set('')
        f.set('')
        time.sleep(0.1)
        g.set(time.strftime('%d/%m/%y'))
    def save():
        bno=a.get()
        bname=b.get()
        if c.get().isalpha()==True:
            Auth=c.get()
        else:
             tkinter.messagebox.showinfo('program',"Enter Correct Author's Name..........")
        date=g.get()
        if e.get().isalpha()==True:
             publ=e.get()
        else:
             tkinter.messagebox.showinfo('program','Enter Correct Publisher Name..........')
        if f.get().isalpha()==False:
            qty=f.get()
        else:
            tkinter.messagebox.showinfo('program','Enter Correct Quantity..........')
        if d.get().isalpha()==False:
            price=d.get()
        else:
            tkinter.messagebox.showinfo('program','Enter Correct Price..........')
        if d.get().isalpha()==False and f.get().isalpha()==False and c.get().isalpha()==True and e.get().isalpha()==True:
            try:
                cnx=sqlite3.connect('Library.db')
                Cr=cnx.cursor()
                data="INSERT INTO BookRecord VALUES"+'('+"'"+str(bno)+"'"+','+"'"+str(bname)+"'"+','+"'"+str(Auth)+"'"+','+"'"+str(price)+"'"+','+"'"+str(publ)+"'"+','+"'"+str(qty)+"'"+','+"'"+str(date)+"'"+')'
                Cr.execute(data)
                cnx.commit()
                Cr.close()
                tkinter.messagebox.showinfo('program','Record Inserted..........')
                reset()
            except sqlite3.Error as err:
                print(err)
 #---------------------------------------------------------------------------
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Name=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Name:\t')
    Member_Name.grid(row=1,column=0)
    Mobil_Number=Label(member,font=('arial 18 bold'),bg='Powder Blue',text="Enter Book Author's Name:\t")
    Mobil_Number.grid(row=2,column=0)
    lab1=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Price:\t')
    lab1.grid(row=5,column=0)
    lab2=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Publisher of Book:\t')
    lab2.grid(row=3,column=0)
    lab3=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Quantity purchased:\t')
    lab3.grid(row=4,column=0)
    Day=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Date\t')
    Day.grid(row=6,column=0)
    #------------------
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=a,width=8,justify=LEFT,bd=8,state=DISABLED)
    Member_Codetxt.grid(row=0,column=1)
    Member_Nametxt=Entry(member,font=('arial 16 bold'),
                         text='Member Code:',textvar=b,width=15,bd=8)
    Member_Nametxt.grid(row=1,column=1)
    Mobil_Numbertxt=Entry(member,font=('arial 16 bold'),textvar=c,width=15,bd=8)
    Mobil_Numbertxt.grid(row=2,column=1)
    lab1txt=Entry(member,font=('arial 16 bold'),textvar=d,width=8,bd=8)
    lab1txt.grid(row=5,column=1)
    lab2txt=Entry(member,font=('arial 16 bold'),textvar=e,width=15,bd=8)
    lab2txt.grid(row=3,column=1)
    lab3txt=Entry(member,font=('arial 16 bold'),textvar=f,width=8,bd=8)
    lab3txt.grid(row=4,column=1)
    Daytxt=Entry(member,font=('arial 16 bold'),textvar=g,width=8,bd=8,state=DISABLED)
    Daytxt.grid(row=6,column=1)
    btn=Button(btnfra,text='Save',font=('arial 16 bold'),command=save,bd=8,pady=5,
               bg='Green',width=10)
    btn.grid(row=7,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=7,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exite,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=7,column=2,sticky='w')
    mem.mainloop()
def deletebook():
    mem1=Tk()
    mem1.title('Library Management System')
    mem1.maxsize(500,300)
    mem1.configure(bg='Powder Blue')
    member=Frame(mem1,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem1,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    mno=StringVar()
    def reset():
        mno.set('')
    def exi():
        mem1.destroy()
    def delete():
        a=mno.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from BookRecord')
        l=c.fetchall()
        d={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6]
        try:
            b=d[a]
            slip=b[0]
            number=b[1]
            adress=b[2]
            cost=b[3]
            date=b[4]
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                Qry=("DELETE FROM BookRecord WHERE Book_Code=%s"%(a))
                Cursor.execute(Qry)
                cnx.commit()
                Cursor.close()
                tkinter.messagebox.showinfo('program',"Record(s) Deleted Successfully........")
                reset()
            except:
                tkinter.messagebox.showinfo('program',"Record(s) does not exist........")
        except:
            tkinter.messagebox.showinfo("program",'No such book code found')
#-----------------------------------------------------------------------------------------------------
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Book Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=mno,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    btn=Button(btnfra,text='Delete',font=('arial 16 bold'),command=delete,bd=8,pady=5,
               bg='Orange',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem1.mainloop()
def mainw():
    root=Tk()
    root.title('Library Management System')
    root.maxsize(1000,500)
    root.minsize(1000,500)
    def er():
        root.destroy()
    frame1=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
    frame1.pack(side=TOP)
    frame2=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10)
    frame2.pack(side=TOP)
    labtit=Label(frame1,text='Library Management System',bg='Cadet Blue',fg='White',font=('arial 40 bold'))
    labtit.grid(row=0,column=0)
    # btn-------------------------------------------
    btn1=Button(frame2,text='Books Management',font=('arial 18 bold'),width=25,bd=8,padx=5,
                pady=5,command=Book_Management_System)
    btn2=Button(frame2,text='Members Management',font=('arial 18 bold'),width=25,bd=8,
                padx=5,pady=5,command=Members_Management_System)
    btn3=Button(frame2,text='issue/Return Book',font=('arial 18 bold'),width=25,bd=8,padx=5,
                pady=5,command=Issue_Management_System)
    btn4=Button(frame2,text='Exit',font=('arial 18 bold'),width=25,bd=8,padx=5,pady=5,command=er)
    btn1.grid(row=0,column=0,sticky='w')
    btn2.grid(row=1,column=0,sticky='w')
    btn3.grid(row=2,column=0,sticky='w')
    btn4.grid(row=3,column=0,sticky='w')
#command================================
def Book_Management_System():
    root1=Tk()
    root1.title('Library Management System')
    root1.maxsize(1000,600)
    root1.minsize(1000,600)
    frame1=Frame(root1,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
    frame1.pack(side=TOP)
    frame2=Frame(root1,bg='Powder Blue',padx=5,pady=5,bd=10)
    frame2.pack(side=TOP)
    labtit=Label(frame1,text='Library Management System',bg='Cadet Blue',fg='White',font=('arial 40 bold'))
    labtit.grid(row=0,column=0)
    # btn  -----------------------------------------------------------------------------
    btn1=Button(frame2,text='Add Book Record',font=('arial 16 bold'),width=20,bd=6,padx=5,
                pady=5,command=insertData)
    btn2=Button(frame2,text='Display Book Records',font=('arial 16 bold'),width=20,bd=6,
                padx=5,pady=5,command=display_b)
    btn3=Button(frame2,text='Search Book Record',font=('arial 16 bold'),width=20,bd=6,
                padx=5,pady=5,command=Searchbook)
    btn4=Button(frame2,text='Delete Book Record',font=('arial 16 bold'),width=20,bd=6,
                padx=5,pady=5,command=deletebook)
    btn5=Button(frame2,text='Update Book Record',font=('arial 16 bold'),width=20,bd=6,
                padx=5,pady=5,command=Updatebook)
    btn6=Button(frame2,text='Return to Main Menu',font=('arial 16 bold'),width=20,bd=6,
                padx=5,pady=5,command=mainw)
    btn1.grid(row=0,column=0,sticky='w')
    btn2.grid(row=1,column=0,sticky='w')
    btn3.grid(row=2,column=0,sticky='w')
    btn4.grid(row=3,column=0,sticky='w')
    btn5.grid(row=4,column=0,sticky='w')
    btn6.grid(row=5,column=0,sticky='w')
    root.destroy()
    root1.mainloop()
def Members_Management_System():
    root2=Tk()
    root2.title('Library Management System')
    root2.maxsize(1000,600)
    root2.minsize(1000,600)
    frame1=Frame(root2,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
    frame1.pack(side=TOP)
    frame2=Frame(root2,bg='Powder Blue',padx=5,pady=5,bd=10)
    frame2.pack(side=TOP)
    labtit=Label(frame1,text='Library Management System',bg='Cadet Blue',fg='White',font=('arial 40 bold'))
    labtit.grid(row=0,column=0)
    # btn -------------------------------------------------------------
    btn1=Button(frame2,text='Add Member Record',font=('arial 16 bold'),width=20,bd=8,
                padx=5,pady=5,command=insertMember)
    btn2=Button(frame2,text='Display Member Records',font=('arial 16 bold'),width=20,bd=8,
                padx=5,pady=5,command=display_m)
    btn3=Button(frame2,text='Search Member Record',font=('arial 16 bold'),width=20,
                bd=8,padx=5,pady=5,command=SearchMember)
    btn4=Button(frame2,text='Delete Member Record',font=('arial 16 bold'),width=20,
                bd=8,padx=5,pady=5,command=deleteMember)
    btn5=Button(frame2,text='Update Member Record',font=('arial 16 bold'),width=20,bd=8,
                padx=5,pady=5,command=UpdateMember)
    btn6=Button(frame2,text='Return to Main Menu',font=('arial 16 bold'),width=20,bd=8,
                padx=5,pady=5,command=mainw)
    btn1.grid(row=0,column=0,sticky='w')
    btn2.grid(row=1,column=0,sticky='w')
    btn3.grid(row=2,column=0,sticky='w')
    btn4.grid(row=3,column=0,sticky='w')
    btn5.grid(row=4,column=0,sticky='w')
    btn6.grid(row=5,column=0,sticky='w')
    root.destroy()
    root2.mainloop()
def Issue_Management_System():
    root3=Tk()
    root3.title('Library Management System')
    root3.maxsize(1000,600)
    root3.minsize(1000,600)
    frame1=Frame(root3,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
    frame1.pack(side=TOP)
    frame2=Frame(root3,bg='Powder Blue',padx=5,pady=5,bd=10)
    frame2.pack(side=TOP)
    labtit=Label(frame1,text='Library Management System',bg='Cadet Blue',fg='White',font=('arial 40 bold'))
    labtit.grid(row=0,column=0)
    # btn------------------------------
    btn1=Button(frame2,text='Issue Book',font=('arial 16 bold'),width=25,bd=10,
                padx=5,pady=5,command=issueBook)
    btn2=Button(frame2,text='Display Issued Book Records',font=('arial 16 bold'),
                width=25,bd=8,padx=5,pady=5,command=showIssueBooks)
    btn3=Button(frame2,text='Return Issue Book',font=('arial 16 bold'),width=25,
                bd=8,padx=5,pady=5,command=returnBook)
    btn4=Button(frame2,text='Return to main menu',font=('arial 16 bold'),width=25,
                bd=8,padx=5,pady=5,command=mainw)
    btn1.grid(row=0,column=0,sticky='w')
    btn2.grid(row=1,column=0,sticky='w')
    btn3.grid(row=2,column=0,sticky='w')
    btn4.grid(row=3,column=0,sticky='w')
    root.destroy()
    root3.mainloop()
def display_m():
    rootdis=Tk()
    rootdis.title('Library Management System')
    rootdis.maxsize(1000,600)
    scrollbar=Scrollbar(rootdis)
    scrollbar.pack(side=RIGHT,fill=Y)
    txtdisplay=Text(rootdis,font=('arial 16 bold'),width=1000,height=800,bd=8)
    txtdisplay.pack(side=BOTTOM)
    try:
        cnx=sqlite3.connect('Library.db')
        Cursor=cnx.cursor()
        query=("SELECT * FROM Member")
        Cursor.execute(query)
        for(Mno,Mname,MOB,DOP,ADR) in Cursor:
            a=Mno
            b=Mname
            c=MOB
            d=DOP
            e=ADR
            txtdisplay.insert(END,"Member Code :-\t\t\t"+str(a)+'\n')
            txtdisplay.insert(END,"Member Name :-\t\t\t"+str(b)+'\n')
            txtdisplay.insert(END,"Mobile No. of Member :-\t\t\t"+str(c)+'\n')
            txtdisplay.insert(END,"Date of Membership :-\t\t\t"+str(d)+'\n')
            txtdisplay.insert(END,"Address :-\t\t\t"+str(e)+'\n')
            txtdisplay.insert(END,"============================================\n")
            scrollbar.config(command=txtdisplay.yview)
            txtdisplay.config(yscrollcommand=scrollbar.set)  
        cnx.commit()
        Cursor.close()
    except sqlite3.Error as err:
        txtdisplay.insert(END,str(err))
        rootdis.mainloop()
def display_b():
    rootdis=Tk()
    rootdis.title('Library Management System')
    rootdis.maxsize(800,500)
    rootdis.maxsize(800,500)
    scrollbar=Scrollbar(rootdis)
    scrollbar.pack(side=RIGHT,fill=Y)
    txtdisplay1=Text(rootdis,font=('arial 16 bold'),width=1000,height=800,bd=8)
    txtdisplay1.pack(side=TOP)
    try:
        cnx=sqlite3.connect('Library.db')
        Cursor=cnx.cursor()
        query=("SELECT * FROM BookRecord")
        Cursor.execute(query)
        for(Book_Code,Book_Name,Book_Author,Book_price,P_Book,Q_Book,Date) in Cursor:
            a=Book_Code
            b=Book_Name
            c=Book_Author
            d=Book_price
            e=P_Book
            f=Q_Book
            g=Date
            txtdisplay1.insert(END,"Book Code:-\t\t\t"+str(a)+'\n')
            txtdisplay1.insert(END,"Book Name:-\t\t\t"+str(b)+'\n')
            txtdisplay1.insert(END,"Author of Book:-\t\t\t"+str(c)+'\n')
            txtdisplay1.insert(END,"Price of Book:-\t\t\t"+str(d)+'\n')
            txtdisplay1.insert(END,"Publisher:-\t\t\t"+str(e)+'\n')
            txtdisplay1.insert(END,"Total Quantity in Hand:-\t\t\t"+str(f)+'\n')
            txtdisplay1.insert(END,"Purchased On:-\t\t\t"+str(g)+'\n')
            txtdisplay1.insert(END,"==========================================\n")
            scrollbar.config(command=txtdisplay1.yview)
            txtdisplay1.config(yscrollcommand=scrollbar.set)  
        cnx.commit()
        Cursor.close()
    except sqlite3.Error as err:
        txtdisplay1.insert(END,str(err))
    rootdis.mainloop()
#except sqlite3.Error as err:
    #print(err)
def insertMember():
    mem=Tk()
    mem.title('Library Management System')
    mem.maxsize(1000,800)
    mem.configure(bg='Powder Blue')
    member=Frame(mem,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    mno=StringVar()
    mname=StringVar()
    mob=StringVar()
    date=StringVar()
    mname1=StringVar()
    date.set(time.strftime('%d/%m/%y'))
    addr=StringVar()
    mno.set(random.randint(100000,999999))
    mname.set('')
    mname1.set('')
    mob.set('')
    addr.set('')
    def exite():
        mem.destroy()
    def reset():
        mno.set(random.randint(100000,999999))
        mname.set('')
        mob.set('') 
        addr.set('')
        mname1.set('')
        time.sleep(0.1)
        date.set(time.strftime('%d/%m/%y'))
    def save():
        a=mno.get()
        if str(mname.get()).isalpha()==True:
            b=mname.get()
        else:
            tkinter.messagebox.showinfo('program','Enter Correct Name ..........')
        if str(mname1.get()).isalpha()==True:
            o=mname1.get()
            f=b+' '+o
        else:
            tkinter.messagebox.showinfo('program','Enter Correct Name ..........')
        if len(str(mob.get()))==10:
            c=mob.get()
        else: 
            tkinter.messagebox.showinfo('program','Enter 10 digits number..........')
        d=date.get()
        g=addr.get()
        if str(mname.get()).isalpha()==True and len(str(mob.get()))==10:
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                Qry="INSERT INTO Member VALUES('%s','%s','%s','%s','%s')"%(a,f,c,d,g)
                Cursor.execute(Qry)
                cnx.commit()
                Cursor.close()
                tkinter.messagebox.showinfo('program','Record Inserted..........')
                reset()
            except sqlite3.Error as e:
                print(e)
        else:
            return None
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text=' Member Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Name1=Label(member,font=('arial 18 bold'),bg='Powder Blue',text=' First Name:\t')
    Member_Name1.grid(row=1,column=0)
    Member_Name2=Label(member,font=('arial 18 bold'),bg='Powder Blue',text=' Last Name:\t')
    Member_Name2.grid(row=2,column=0)
    Mobil_Number=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Mobile Number:\t')
    Mobil_Number.grid(row=3,column=0)
    ADr=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Address:\t')
    ADr.grid(row=4,column=0,sticky='w')
    Day=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Date:\t\t')
    Day.grid(row=5,column=0)
    #-------------------------------------------------------
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=mno,width=8,justify=LEFT,bd=8,state=DISABLED)
    Member_Codetxt.grid(row=0,column=1)
    Member_Nametxt=Entry(member,font=('arial 16 bold'),
                         textvar=mname,width=15,bd=8)
    Member_Nametxt.grid(row=1,column=1)
    Member_Nametxt1=Entry(member,font=('arial 16 bold'),
                         textvar=mname1,width=15,bd=8)
    Member_Nametxt1.grid(row=2,column=1)
    Mobil_Numbertxt=Entry(member,font=('arial 16 bold'),textvar=mob,width=15,bd=8)
    Mobil_Numbertxt.grid(row=3,column=1)
    ADrtxt=Entry(member,font=('arial 18 bold'),textvar=addr,width=15,bd=8)
    ADrtxt.grid(row=4,column=1)
    Daytxt=Entry(member,font=('arial 16 bold'),textvar=date,width=8,bd=8,state=DISABLED)
    Daytxt.grid(row=5,column=1)
    btn=Button(btnfra,text='Save',font=('arial 16 bold'),command=save,bd=8,pady=5,
               bg='Green',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exite,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem.mainloop()
def SearchMember():
    mem21=Tk()
    mem21.title('Library Management System')
    mem21.maxsize(500,600)
    mem21.configure(bg='Powder Blue')
    h=StringVar()
    member=Frame(mem21,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem21,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    txtdispla1=Text(mem21,font=('arial 16 bold'),width=500,height=400,bd=8)
    txtdispla1.pack(side=LEFT)
    def search():
        g=h.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from Member')
        l=c.fetchall()
        d={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4]
        try:
            b=d[g]
            member=b[0]
            number=b[1]
            adress=b[2]
            date=b[3]
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                query="SELECT * FROM Member WHERE Mno='%s'"%(g)
                Cursor.execute(query)
                for (Mno,Mname,MOB,DOP,ADR) in Cursor:
                    a1=Mno
                    b1=Mname
                    c1=MOB
                    d1=DOP
                    e1=ADR
                    txtdispla1.insert(END,"Member Code :-\t\t\t"+str(a1)+'\n')
                    txtdispla1.insert(END,"Member Name :-\t\t\t"+str(b1)+'\n')
                    txtdispla1.insert(END,"Mobile No. of Member :-\t\t\t"+str(c1)+'\n')
                    txtdispla1.insert(END,"Date of Membership :-\t\t\t"+str(d1)+'\n')
                    txtdispla1.insert(END,"Address :-\t\t\t"+str(e1)+'\n')
                cnx.commit()
                Cursor.close()    
            except:
                 tkinter.messagebox.showinfo('program','Member  Code does not exist ..........')
        except:
            tkinter.messagebox.showinfo('program','Member  Code does not exist ..........')
    def reset():
        h.set('')
        txtdispla1.delete('0.0',END)
    def exi():
        mem21.destroy()        
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Member Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=h,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    btn=Button(btnfra,text='Search',font=('arial 16 bold'),command=search,bd=8,pady=5,bg='Orange',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem21.mainloop()
def UpdateMember():
    mem=Tk()
    mem.title('Library Management System')
    mem.maxsize(500,400)
    mem.configure(bg='Powder Blue')
    member=Frame(mem,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    bn=StringVar()
    mname=StringVar()
    mob=StringVar()
    date=StringVar()
    addr=StringVar()
    mname1=StringVar()
    mname.set('')
    mob.set('')
    addr.set('')
    mname1.set('')
    def reset():
        a.set(random.randint(1000,9999))
        b.set('')
        c.set('')
        d.set('')
        e.set('')
        f.set('')
        g.set(time.strftime('%d/%m/%y')) 
    def exite():
        mem.destroy()
    def reset():
        bn.set('')
        mname.set('')
        mob.set('') 
        addr.set('')
        mname1.set('')
        date.set('')
    def update():
        a=bn.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from Member')
        l=c.fetchall()
        d={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4]
        try:
            b=d[a]
            member=b[0]
            number=b[1]
            adress=b[2]
            dat=b[3]
            if str(mname.get()).isalpha()==True:
                b=mname.get()
            else:
                tkinter.messagebox.showinfo('program','Enter Correct First Name ..........')
            if str(mname1.get()).isalpha()==True:
                o=mname1.get()
                f=b+' '+o
            else:
                tkinter.messagebox.showinfo('program','Enter Correct Second Name ..........')
            if len(str(mob.get()))==10:
                c=mob.get()
            else: 
                tkinter.messagebox.showinfo('program','Enter 10 digits number..........')
            d=date.get()
            g=addr.get()
            if str(mname.get()).isalpha()==True and len(str(mob.get()))==10:
                try:
                    cnx=sqlite3.connect('Library.db')
                    Cursor=cnx.cursor()
                    query=("SELECT * FROM Member WHERE MNO=%s"%(a))
                    Cursor.execute(query)
                    Qry="UPDATE Member SET Mname='%s',MOB='%s',DOP='%s',ADR='%s' WHERE Mno='%s'"%(f,c,d,g,a)                                                                               
                    Cursor.execute(Qry)
                    cnx.commit()
                    Cursor.close()
                    tkinter.messagebox.showinfo('program',"Records Updated Successfully......")
                    reset()
                except:
                   tkinter.messagebox.showinfo('program','Member  Code does not exist ..........') 
            else:
                return None
        except:
            tkinter.messagebox.showinfo('program','Member  Code does not exist ..........')
   
    
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Member Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=bn,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    Member_Name=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Member Name:\t')
    Member_Name.grid(row=1,column=0)
    Member_Name2=Label(member,font=('arial 18 bold'),bg='Powder Blue',text=' Last Name:\t')
    Member_Name2.grid(row=2,column=0)
    Member_Nametxt1=Entry(member,font=('arial 16 bold'),
                         textvar=mname1,width=15,bd=8)
    Member_Nametxt1.grid(row=2,column=1)
    Mobil_Number=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Mobile Number:\t')
    Mobil_Number.grid(row=3,column=0)
    ADr=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Address:\t')
    ADr.grid(row=4,column=0,sticky='w')
    Day=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Date:\t\t')
    Day.grid(row=5,column=0)
    #----------------------------------------------------
    Member_Nametxt=Entry(member,font=('arial 16 bold'),
                         text='Member Code:',textvar=mname,width=15,bd=8)
    Member_Nametxt.grid(row=1,column=1)
    Mobil_Numbertxt=Entry(member,font=('arial 16 bold'),textvar=mob,width=15,bd=8)
    Mobil_Numbertxt.grid(row=3,column=1)
    ADrtxt=Entry(member,font=('arial 18 bold'),textvar=addr,width=15,bd=8)
    ADrtxt.grid(row=4,column=1)
    Daytxt=Entry(member,font=('arial 16 bold'),textvar=date,width=8,bd=8)
    Daytxt.grid(row=5,column=1)
    btn=Button(btnfra,text='Update',font=('arial 16 bold'),command=update,bd=8,pady=5,
               bg='Orange',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exite,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem.mainloop()
def deleteMember():
    mem1=Tk()
    mem1.title('Library Management System')
    mem1.maxsize(500,300)
    mem1.configure(bg='Powder Blue')
    member=Frame(mem1,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem1,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    mno=StringVar()
    def reset():
        mno.set('')
    def exi():
        mem1.destroy()
    def deletei():
        a=mno.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from Member')
        l=c.fetchall()
        d={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4]
        try:
            b=d[a]
            member=b[0]
            number=b[1]
            adress=b[2]
            date=b[3]
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                Qry=("DELETE FROM Member WHERE Mno=%s"%(a))
                Cursor.execute(Qry)
                cnx.commit()
                Cursor.close()
                tkinter.messagebox.showinfo('program',"Record(s) Deleted Successfully........")
                reset()
            except:
                tkinter.messagebox.showinfo('program','Member  Code does not exist ..........')
        except:
            tkinter.messagebox.showinfo('program','Member  Code does not exist ..........')
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Member Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=mno,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    btn=Button(btnfra,text='Delete',font=('arial 16 bold'),command=deletei,bd=8,pady=5,
               bg='Orange',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem1.mainloop() 
    #2nd window-----------------------------------------------------------
def Searchbook():
    mem2=Tk()
    mem2.title('Library Management System')
    mem2.maxsize(500,500)
    mem2.configure(bg='Powder Blue')
    member=Frame(mem2,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem2,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    txtdispla=Text(mem2,font=('arial 16 bold'),width=500,height=400,bd=8)
    txtdispla.pack(side=LEFT)
    mnm=StringVar()
    def reset():
        mnm.set('')
        txtdispla.delete('0.0',END)
    def exi():
        mem2.destroy()
    def search():
        a=mnm.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from BookRecord')
        l=c.fetchall()
        d={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6]
        try:
            b=d[a]
            slip=b[0]
            number=b[1]
            adress=b[2]
            cost=b[3]
            date=b[4]
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                query=("SELECT * FROM BookRecord WHERE Book_Code=%s"%(a))
                Cursor.execute(query)
                for(Book_Code,Book_Name,Book_Author,Book_price,P_Book,Q_Book,Date) in Cursor:
                    a=Book_Code
                    b=Book_Name
                    c=Book_Author
                    d=Book_price
                    e=P_Book
                    f=Q_Book
                    g=Date
                    txtdispla.insert(END,"Book Code:-\t\t\t"+str(a)+'\n')
                    txtdispla.insert(END,"Book Name:-\t\t\t"+str(b)+'\n')
                    txtdispla.insert(END,"Author of Book:-\t\t\t"+str(c)+'\n')
                    txtdispla.insert(END,"Pulisher:-\t\t\t"+str(e)+'\n')
                    txtdispla.insert(END,"Price of Book:-\t\t\t"+str(d)+'\n')
                    txtdispla.insert(END,"Total Quantity in Hand:-\t\t\t"+str(f)+'\n')
                    txtdispla.insert(END,"Purchased On:-\t\t\t"+str(g)+'\n')
                cnx.commit()
                Cursor.close()  
            except:
                tkinter.messagebox.showinfo('program','Book Code does not exist ..........')
        except:
            tkinter.messagebox.showinfo('program','Book Code does not exist ..........')
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Book Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=mnm,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    btn=Button(btnfra,text='Search',font=('arial 16 bold'),command=search,bd=8,pady=5,
               bg='Orange',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem2.mainloop()
def Updatebook():
    mem=Tk()
    mem.title('Library Management System')
    mem.maxsize(700,700)
    mem.configure(bg='Powder Blue')
    member=Frame(mem,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    Book_Code=StringVar()
    Book_Name=StringVar()
    Book_Author=StringVar()
    Book_price=StringVar()
    P_Book=StringVar()
    Q_Book=StringVar()
    Date=StringVar()
    def exite():
        mem.destroy()
    def reset():
        Book_Code.set('')
        Book_Name.set('')
        Book_Author.set('') 
        Book_price.set('')
        P_Book.set('')
        Q_Book.set('')
        Date.set('')
    def update():
        a=Book_Code.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from BookRecord')
        l=c.fetchall()
        d={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6]
        try:
            b=d[a]
            slip=b[0]
            number=b[1]
            adress=b[2]
            cost=b[3]
            date=b[4]
            b=Book_Name.get()
            c=Book_Author.get()
            d=Book_price.get()
            e=P_Book.get()
            f=Q_Book.get()
            g=Date.get()
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                query=("SELECT * FROM BookRecord WHERE Book_Code=%s"%(a))
                Cursor.execute(query)
                Qry="UPDATE BookRecord SET Book_Name='%s',Book_Author='%s',Book_price='%s',P_Book='%s',Q_Book='%s',Date='%s' WHERE Book_Code='%s'"%(b,c,d,e,f,g,a)                                                                               
                Cursor.execute(Qry)
                cnx.commit()
                Cursor.close()
                tkinter.messagebox.showinfo('program',"Records Updated Successfully......")
                reset()
            except:
                tkinter.messagebox.showinfo('program','Book Code does not exist ..........')
        except:
            tkinter.messagebox.showinfo('program','Book Code does not exist ..........')
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Name=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Name:\t')
    Member_Name.grid(row=1,column=0)
    Mobil_Number=Label(member,font=('arial 18 bold'),bg='Powder Blue',text="Enter Book Author's Name:\t")
    Mobil_Number.grid(row=2,column=0)
    lab1=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Price:\t')
    lab1.grid(row=3,column=0)
    lab2=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Publisher of Book:\t')
    lab2.grid(row=4,column=0)
    lab3=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Quantity purchased:\t')
    lab3.grid(row=5,column=0)
    Day=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Date\t')
    Day.grid(row=6,column=0)
    #------------------
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=Book_Code,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    Member_Nametxt=Entry(member,font=('arial 16 bold'),
                         text='Member Code:',textvar=Book_Name,width=15,bd=8)
    Member_Nametxt.grid(row=1,column=1)
    Mobil_Numbertxt=Entry(member,font=('arial 16 bold'),textvar=Book_Author,width=15,bd=8)
    Mobil_Numbertxt.grid(row=2,column=1)
    lab1txt=Entry(member,font=('arial 16 bold'),textvar=Book_price,width=8,bd=8)
    lab1txt.grid(row=3,column=1)
    lab2txt=Entry(member,font=('arial 16 bold'),textvar=P_Book,width=15,bd=8)
    lab2txt.grid(row=4,column=1)
    lab3txt=Entry(member,font=('arial 16 bold'),textvar=Q_Book,width=8,bd=8)
    lab3txt.grid(row=5,column=1)
    Daytxt=Entry(member,font=('arial 16 bold'),textvar=Date,width=8,bd=8)
    Daytxt.grid(row=6,column=1)
    btn=Button(btnfra,text='Update',font=('arial 16 bold'),command=update,bd=8,pady=5,
               bg='Orange',width=10)
    btn.grid(row=4,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=4,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exite,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=4,column=2,sticky='w')
    mem.mainloop()
def showIssueBooks():
    rootdis=Tk()
    rootdis.title('Library Management System')
    rootdis.maxsize(1000,600)
    scrollbar=Scrollbar(rootdis)
    scrollbar.pack(side=RIGHT,fill=Y)
    txtdisplay1=Text(rootdis,font=('arial 16 bold'),width=1000,height=800,bd=8)
    txtdisplay1.pack(side=TOP)       
    try:
        os.system('cls')
        cnx=sqlite3.connect('Library.db')
        Cursor=cnx.cursor()
        a=StringVar()
        Query=("SELECT B.Book_Code,B.Book_Name,M.Mno,M.Mname,I.d_o_issue,I.d_o_ret FROM BookRecord B,Issue I,Member M where I.bno=B.Book_Code and I.mno=M.Mno")
        Cursor.execute(Query)
        for (Bno,Bname,Mno,Mname,doi,dor) in Cursor:
            a=Bno
            b=Bname
            c=Mno
            d=Mname
            e=doi
            f=dor
            txtdisplay1.insert(END,"Book Code:-\t\t\t"+str(a)+'\n')
            txtdisplay1.insert(END,"Book Name:-\t\t\t"+str(b)+'\n')
            txtdisplay1.insert(END,"Member Code:-\t\t\t"+str(c)+'\n')
            txtdisplay1.insert(END,"Member Name:-\t\t\t"+str(d)+'\n')
            txtdisplay1.insert(END,"Date of issue:-\t\t\t"+str(e)+'\n')
            txtdisplay1.insert(END,"Date of return:-\t\t\t"+str(f)+'\n')
            txtdisplay1.insert(END,"======================================\n")
            scrollbar.config(command=txtdisplay1.yview)
            txtdisplay1.config(yscrollcommand=scrollbar.set)  
            cnx.commit()
            #Cursor.close()
    except sqlite3.Error as err:
        print(err)
    rootdis.mainloop()
def issueBook():
    mem=Tk()
    mem.title('Library Management System')
    mem.maxsize(1000,800)
    mem.configure(bg='Powder Blue')
    member=Frame(mem,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    a=StringVar()
    b=StringVar()
    date=StringVar()
    date.set(time.strftime('%d/%m/%y'))
    a.set('')
    b.set('')
    def exi():
        mem.destroy()
    def reset():
        date.set(time.strftime('%d/%m/%y'))
        a.set('')
        b.set('')
    def save():
        bno=a.get()
        mno=b.get()
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from BookRecord')
        l=c.fetchall()
        c.execute('select* from Member')
        l2=c.fetchall()
        d={}
        d2={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6]
        for row1 in l2:
            d2[row1[0]]=row1[1],row1[2],row1[3],row1[4]
        try:
            b2=d[bno]
            b1=d2[mno]
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                z=date.get()
                Qry=("INSERT INTO Issue(bno,mno,d_o_issue)VALUES('%s','%s','%s')"%(bno,mno,z))
                Cursor.execute(Qry)
                cnx.commit()
                Cursor.close()
                tkinter.messagebox.showinfo('program',"Book Issued Successfully........")
            except:
                tkinter.messagebox.showinfo('program',"Book Code  or Member Code does not found")
        except:
            tkinter.messagebox.showinfo('program',"Book Code or Member Code  does not found")
    def reset():
        a.set(random.randint(1000,9999))
        b.set('')
        c.set('')
        d.set('')
        e.set('')
        f.set('')
        g.set(time.strftime('%d/%m/%y'))            
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Name=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Member Code:\t')
    Member_Name.grid(row=1,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=a,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    Member_Nametxt=Entry(member,font=('arial 16 bold'),
                         text='Member Code:',textvar=b,width=15,bd=8)
    Member_Nametxt.grid(row=1,column=1)
    Day=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Date:\t\t')
    Day.grid(row=2,column=0)
    Daytxt=Entry(member,font=('arial 16 bold'),textvar=date,width=8,bd=8,state=DISABLED)
    Daytxt.grid(row=2,column=1)
    btn=Button(btnfra,text='Save',font=('arial 16 bold'),command=save,bd=8,pady=5,
               bg='Green',width=10)
    btn.grid(row=7,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=7,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=7,column=2,sticky='w')
    mem.mainloop()
def returnBook():
    mem=Tk()
    mem.title('Library Management System')
    mem.maxsize(1000,800)
    mem.configure(bg='Powder Blue')
    member=Frame(mem,bg='Powder Blue',bd=5)
    member.pack(side=TOP)
    btnfra=Frame(mem,bg='Powder Blue',bd=5)
    btnfra.pack(side=BOTTOM)
    a=StringVar()
    b=StringVar()
    date=StringVar()
    a.set('')
    b.set('')
    date.set(time.strftime('%d/%m/%y'))
    def exi():
        mem.destroy()
    def reset():
        a.set('')
        b.set('')
        date.set(time.strftime('%d/%m/%y'))
    def save():
        bno=a.get()
        Mno=b.get()
        
        crr=sqlite3.connect('Library.db')
        c=crr.cursor()
        c.execute('select* from BookRecord')
        l=c.fetchall()
    
        c.execute('select* from Member')
        l2=c.fetchall()
        
        d={}
        d2={}
        for row in l:
            d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6]
        for row1 in l2:
            d2[row1[0]]=row1[1],row1[2],row1[3],row1[4]
        try:
            b2=d[bno]
            
            b1=d2[Mno]
            try:
                cnx=sqlite3.connect('Library.db')
                Cursor=cnx.cursor()
                bno=a.get()
                Mno=b.get()
                recDate=str(time.strftime('%d/%m/%y'))
                Qry=("Update Issue set d_o_ret='%s' WHERE bno='%s' and mno='%s'"%(recDate,bno,Mno))
                Cursor.execute(Qry)
                #Make sure data is comitted to the database cnx.commit()
                cnx.commit()
                Cursor.close()
                tkinter.messagebox.showinfo('Program',"Book Returned Successfully.........")
            except:
                tkinter.messagebox.showinfo('program','Book Code or Member Code does not match')
        except:
            tkinter.messagebox.showinfo('program','Book Code or Member Code does not match')
    Member_Code=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Book Code:\t')
    Member_Code.grid(row=0,column=0)
    Member_Name=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Enter Member Code:\t')
    Member_Name.grid(row=1,column=0)
    Member_Codetxt=Entry(member,font=('arial 16 bold'),textvar=a,width=8,justify=LEFT,bd=8)
    Member_Codetxt.grid(row=0,column=1)
    Member_Nametxt=Entry(member,font=('arial 16 bold'),
                         text='Member Code:',textvar=b,width=15,bd=8)
    Member_Nametxt.grid(row=1,column=1)
    Day=Label(member,font=('arial 18 bold'),bg='Powder Blue',text='Date:\t\t')
    Day.grid(row=2,column=0)
    Daytxt=Entry(member,font=('arial 16 bold'),textvar=date,width=8,bd=8)
    Daytxt.grid(row=2,column=1)
    btn=Button(btnfra,text='Return',font=('arial 16 bold'),command=save,bd=8,pady=5,
               bg='Green',width=10)
    btn.grid(row=7,column=0,sticky='w')
    btn1=Button(btnfra,text='Reset',font=('arial 16 bold'),command=reset,bd=8,
                pady=5,bg='Yellow',width=10)
    btn1.grid(row=7,column=1,sticky='w')
    btn2=Button(btnfra,text='Exit',font=('arial 16 bold'),command=exi,bd=8,
                pady=5,bg='Red',width=10)
    btn2.grid(row=7,column=2,sticky='w')
    mem.mainloop()           
# btn--------------------------------------------------------------------
frame1=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
frame1.pack(side=TOP)
frame12=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
frame12.pack(side=LEFT)
frame13=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
frame13.pack(side=RIGHT)
frame2=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10)
frame2.pack(side=TOP)
frame21=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10)
frame21.pack(side=BOTTOM)
frame21=Frame(root,bg='Powder Blue',padx=5,pady=5,bd=10,relief=RIDGE)
frame21.pack(side=BOTTOM)
#====================================================
labtit=Label(frame1,text='Library Management System',bg='Cadet Blue',fg='White',font=('arial 40 bold'))
labtit.grid(row=0,column=0)
#photo
photod1=PhotoImage(file='h4.png')
photo_labeld1=Label(frame12,image=photod1)
photo_labeld1.pack(side=TOP,fill=BOTH)
photod2=PhotoImage(file='h7.png')
photo_labeld2=Label(frame13,image=photod2)
photo_labeld2.pack(side=TOP,fill=BOTH)
photod3=PhotoImage(file='h1.png')
photo_labeld3=Label(frame12,image=photod3)
photo_labeld3.pack(side=TOP,fill=BOTH)
photod4=PhotoImage(file='h2.png')
photo_labeld4=Label(frame12,image=photod4)
photo_labeld4.pack(side=TOP,fill=BOTH)
photod5=PhotoImage(file='h3.png')
photo_labeld5=Label(frame13,image=photod5)
photo_labeld5.pack(side=TOP,fill=BOTH)
photod6=PhotoImage(file='h6.png')
photo_labeld6=Label(frame13,image=photod6)
photo_labeld6.pack(side=TOP,fill=BOTH)
photod7=PhotoImage(file='h5.png')
photo_labeld7=Label(frame21,image=photod7)
photo_labeld7.pack(side=BOTTOM,fill=BOTH)
# btn -----------------------------------------------------------------
btn1=Button(frame2,text='Books Management',font=('arial 18 bold'),width=25,bd=8,padx=5,
            pady=5,command=Book_Management_System)
btn2=Button(frame2,text='Members Management',font=('arial 18 bold'),width=25,bd=8,
            padx=5,pady=5,command=Members_Management_System)
btn3=Button(frame2,text='issue/Return Book',font=('arial 18 bold'),width=25,bd=8,padx=5,
            pady=5,command=Issue_Management_System)
btn4=Button(frame2,text='Exit',font=('arial 18 bold'),width=25,bd=8,padx=5,pady=5,command=iExit)
btn1.pack(side=TOP,fill=BOTH)
btn2.pack(side=TOP,fill=BOTH)
btn3.pack(side=TOP,fill=BOTH)
btn4.pack(side=TOP,fill=BOTH)
root.mainloop()
#--------------------------------------------- THE END --------------------------------------
