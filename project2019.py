from tkinter import*
import mySQL.connector

def onclick1():
    id=entryid.get()
    name=entryname.get()
    phone=entryphone.get()
    email=entryemail.get()

print(id,name,phone,email)

SQL="insert into customer values(null,'{}','{}','{}','{}')".format(id,name,phone,email)

con=mySQL.connector.connect(users="root",password="",host="localhost",database="IT")

cursor=con.cursor()
cursor.execute(SQL)
con.commit()

def onclick2():
    id = entryid.get()
    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()

print(id,name,phone,email)

SQL="update customer setname=(null,'{}') where id=(null,'{}')".format(name,id)

con=mySQL.connector.connect(users="root",password="",host="localhost",database="IT")

cursor=con.cursor()
cursor.execute(SQL)
con.commit()

def onclick3():
    id = entryid.get()
    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()

print(id,name,phone,email)

SQL="select * from customer"

con=mySQL.connector.connect(users="root",password="",host="localhost",database="IT")

cursor=con.cursor()
cursor.execute(SQL)


def onclick4():
    id = entryid.get()
    name = entryname.get()
    phone = entryphone.get()
    email = entryemail.get()

print(id,name,phone,email)

SQL="delete from customer where id=(null,'{}')".format(id)


con=mySQL.connector()
cursor.execute(SQL)
con.commit()

window=tk()
untitle=Label(window,taxt="customer information")
intitle.grid(row=0,column=0,colspan)

untitle=Label(window,text="add customer")
untitle.grid(row=1,column=0,pady=10)

unName=Label(window,text="enter customer name")
unName.grid(row=2,column=0,pady=10)

entryname=Entry(window)
entryname.grid(row=2,column=1,pady=10)

unPhone=Label(window,text="enter customer Phone")
unPhone.grid(row=3,column=1,pady=10)

entryPhone=Entry(window)
entryPhone.grid(row=3,column=1,pady=10)

unEmail=Label(window,text="enter customer E-mail")
unEmail.grid(row=4,column=0,pady=10)

entryEmail=Entry(window)
entryEmail.grid(row=4,column=1,pady=10)

btnSave=Button(window,taxt="save customer",command=onclick1)
btnSave.grid(row=5,column=0,pady=20)

uktitle=Label(window,text="update customer")
uktitle.grid(row=1,column=2,pady=10)

ukname=Label(window,text="enter customer NewName")
ukname.grid(row=2,column=2,pady=10)

entryname=Entry(window)
entryname.grid(row=2,column=3,pady=10)

ukid=Label(window,text="enter old customer nameid")
uk.grid(row=2,column=5,pady=10)

btnupdate=Button(window,text="update customer name",command=onclick2)
btnupdate.grid(grid=3,column=2,pady=10)

pltitle=Label(window,text="To view complete data CLICK ON ME")
pktitle.grid(row=4,column=2,pady=20)

btnView=Button(window,text="View data",command=onclick3)
btnView.grid(row=5,column=2,pady=10)

ustitle=label(window,text="to delete particular customer")
ustitle.grid(row,column=2,pady=20)

btndelete=Button(window,text="delete",command=onclick4)
btndelete.grid(row=6,column=2,pady=10)

window.mainloop()


