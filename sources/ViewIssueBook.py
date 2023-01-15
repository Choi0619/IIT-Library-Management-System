from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import cx_Oracle

# try to connect with oracle database
try:
    con = cx_Oracle.connect('c##atest/1234@localhost:1521/xe')
    cur = con.cursor()
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

def ViewIssue():
    # create an interface
    root = Tk()
    root.title("Issued Book")
    root.minsize(width=400,height=400)
    root.geometry("800x500")

    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#87cefa")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Issued Book", bg='black', fg='white', font = ('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    # labeling with format
    Label(labelFrame, text="%-20s%-20s%-30s%-30s%-30s"%('Customer ID','Book ID','Issue date','Return Date', 'Staff ID'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "-------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)

    # SQL command to select data from issue table
    getIssue = "SELECT * FROM Issue"
    try:
        cur.execute(getIssue)
        con.commit()

        for i in cur:
            Label(labelFrame,text="%-20s%-20s%-30s%-30s%-30s"%(i[0],i[1],i[2],i[3],i[4]) ,bg='black', fg='white').place(relx=0.07,rely=y)

            y += 0.1
    except:
        messagebox.showinfo("Failed", "No data retrieved from Issued Books")

    # Quit Button
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
