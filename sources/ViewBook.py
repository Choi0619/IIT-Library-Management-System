from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle

try:
    con = cx_Oracle.connect('c##atest/1234@localhost:1521/xe')
    cur = con.cursor()

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

    # Enter Table Names here


def ViewBook():
    # create an interface
    root = Tk()
    root.title("View Book")
    root.minsize(width=400,height=400)
    root.geometry("1200x700")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#AAA4DD")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFCC55",bd=5)
    headingFrame1.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.55)
    y = 0.25

    Label(labelFrame, text="%-15s%-20s\t%-30s\t%-40s\t%-30s\t%-15s"%('BookID','Publisher ID','Title','Author','ISBN','Available'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)

    # Find from issue table where return_date is null
    unreturned_book = "SELECT * FROM ISSUE WHERE Return_date is NULL"    
    cur.execute(unreturned_book)
    con.commit()
    unreturned_list = [] # list for calculation
    for i in cur:
        unreturned_list.append(i[1]) # add to list where return_date is null
    
    # Use SQL command to select data from books
    getBooks = "SELECT * FROM Books"
    try:
        cur.execute(getBooks)
        con.commit()
        
        for i in cur:
            available = i[5] # index for how many books available
            if i[0] in unreturned_list:
                available -= unreturned_list.count(i[0]) # subtract from book availability
            if available == 0:
                available = "N/A" # if no book available, shows that book is N/A
            Label(labelFrame,text="%-15s%-20s\t\t%-30s\t%-40s\t%-30s\t%-15s"%(i[0],i[1],i[2],i[3],i[4], available) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
            
    except:
        messagebox.showinfo("Failed to fetch files from database")

    # Quit Button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
