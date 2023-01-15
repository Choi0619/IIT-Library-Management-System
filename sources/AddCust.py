from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle


def CustRegister():
    Reg_id = bookInfo1.get()
    Name = bookInfo2.get()
    Email_ID = bookInfo3.get()
    City = bookInfo4.get()
    Contact = bookInfo5.get()
    
    # Insert data to the Table
    in_data = f"'{Reg_id}', '{Name}', '{Email_ID}', '{City}', '{Contact}'"
    try:
        cur.execute(f"INSERT INTO Customer VALUES({in_data})")
        con.commit() 
        messagebox.showinfo("Success","Customer added successfully!")
    except:
        messagebox.showinfo("Error","Can't add data into Database")

    root.destroy()


def addCust(): 
    
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, bookInfo5,  Canvas1, con, cur,bookTable, root
    
    root = Tk()
    root.title("Add New Customer")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    #try to connect with oracle database
    try:
        con = cx_Oracle.connect('c##atest/1234@localhost:1521/xe')
        cur = con.cursor()

    
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)

    bookTable = "Books" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#995599")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#CCBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Customer", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    lb1 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # Publisher ID
    lb2 = Label(labelFrame,text="Name: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Title
    lb3 = Label(labelFrame,text="Email ID : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb4 = Label(labelFrame,text="City : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book ISBN
    lb5 = Label(labelFrame,text="Contact", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.6, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
        
    # Submit Button
    SubmitBtn = Button(root,text="ADD",bg='#d1ccc0', fg='black',command=CustRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit Button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
