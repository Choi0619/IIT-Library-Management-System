from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle


def bookRegister():
    bid = bookInfo1.get()
    pubid = bookInfo2.get()
    title = bookInfo3.get()
    author = bookInfo4.get()
    ISBN = bookInfo5.get()
    Num_of_Books = bookInfo6.get()

    # Insert data to the Table
    in_data = f"{bid}, '{pubid}', '{title}', '{author}', '{ISBN}', {Num_of_Books}"
    try:
        cur.execute(f"INSERT INTO Books VALUES({in_data})")
        con.commit()
        messagebox.showinfo("Success","Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    root.destroy()
    con.close()


def addBook(): 
    global bookInfo1 ,bookInfo2, bookInfo3, bookInfo4, bookInfo5, bookInfo6, Canvas1, con, cur,bookTable, root
    
    # create an interface
    root = Tk()
    root.title("Add Book")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # try to connect with oracle database
    try:
        con = cx_Oracle.connect('c##atest/1234@localhost:1521/xe')
        cur = con.cursor()
    
    except cx_Oracle.DatabaseError as e:
        print("There is a problem with Oracle", e)

    bookTable = "Books" # Book Table

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#9bdd32")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#00BB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Book ID
    book_id = '1' # default value 1
    query = '''select book_ID from books order by book_ID desc fetch first 1 row only''' # find the biggest Book_ID number created from the table
    
    try:
        cur.execute(query)
        con.commit()
        print('Successfully access to book_ID from Oracle')
        for i in cur:
            data = i[0]
            book_id = data + 1 # add 1 to book_ID when new book is added
            
        
    except cx_Oracle.DatabaseError as e:
        print("There is a problem retrieve data from Oracle", e)
        
        
    lb1 = Label(labelFrame,text=f"Book ID : {book_id}", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        


    # Publisher ID
    lb2 = Label(labelFrame,text="Publisher ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Title
    lb3 = Label(labelFrame,text="Title : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.4, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.08)
        
    # Book Author
    lb4 = Label(labelFrame,text="Author : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # Book ISBN
    lb5 = Label(labelFrame,text="ISBN", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.6, relheight=0.08)
        
    bookInfo5 = Entry(labelFrame)
    bookInfo5.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)

    # No. of books
    lb6 = Label(labelFrame,text="No. of books", bg='black', fg='white')
    lb6.place(relx=0.05,rely=0.7, relheight=0.08)
        
    bookInfo6 = Entry(labelFrame)
    bookInfo6.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    #Quit Button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
