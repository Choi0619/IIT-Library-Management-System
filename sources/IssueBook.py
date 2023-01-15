from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle

def bookissue():
    
    Cust_id = bookInfo1.get()
    Book_id = bookInfo2.get()
    Issue_date = bookInfo3.get()
    Return_date = bookInfo4.get()
    Staff_id = bookInfo5.get()
    
    # insert data into the database
    in_data = """INSERT into Issue values (:1,:2,:3,:4,:5)"""
    try:
        cur.execute(in_data, [Cust_id, Book_id, Issue_date, Return_date, Staff_id])
        con.commit() 
        messagebox.showinfo('Success',"Book Issued successfully! Please return it on time")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    root.destroy()
    con.close()


def issueBook(): 
    
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, bookInfo5, Canvas1, con, cur,bookTable, root

    # create an interface
    root = Tk()
    root.title("Issue Book")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    try:
    
        con = cx_Oracle.connect('c##atest/1234@localhost:1521/xe')
        cur = con.cursor()
    
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)

    bookTable = "Issue" # Book Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ffff66")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.35)
        
    # Book ID
    lb1 = Label(labelFrame,text="Customer ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # Publisher ID
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Title
    lb3 = Label(labelFrame,text="Issue Date : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb4 = Label(labelFrame,text="Return Date : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)


    # No. of books
    lb5 = Label(labelFrame,text="Staff ID:", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.6, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
        
    #ISSUE Button
    SubmitBtn = Button(root,text="ISSUE",bg='#d1ccc0', fg='black',command=bookissue)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    # Quit Button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
