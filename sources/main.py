from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
import cx_Oracle
from AddBook import *
from ViewBook import *
from IssueBook import *
from ViewIssueBook import *
from AddCust import *


# environment variable setting for the app
LOCATION = r"C:\instantclient_21_7"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

# Try to connet Oracle with Python
try:
    con = cx_Oracle.connect('c##atest/1234@localhost:1521/xe')
    cursor = con.cursor()
    print(f"Your Oracle version is: {con.version}")
    print("Successfully connected with Oracle database.")

  
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)


# Tkinter front-end interface
root = Tk()
root.title("Library Management System")
root.minsize(width=500,height=500)
root.geometry("700x700")

n=0.25 # sizing


# Adding a background image
background_image =Image.open("background.png")
[imageSizeWidth, imageSizeHeight] = background_image.size

backgroundWidth = int(imageSizeWidth*n*4)
backgroundHeight = int(imageSizeHeight*n*4) 
    
background_image = background_image.resize((backgroundWidth,backgroundHeight),Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = backgroundWidth, height = backgroundHeight)
Canvas1.pack(expand=True,fill=BOTH)

# Setting up header frame 
headingFrame1 = Frame(root,bg="#333333",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to IIT\nLibrary Management System", bg='white', fg='brown', font=('Courier',16))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

# Adding up buttons to click

btn1 = Button(root,text="Add Book",bg='red', fg='white', command = addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.08)

btn2 = Button(root,text="Add New Customer",bg='orange', fg='black', command = addCust)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.08)
    
btn3 = Button(root,text="View Book List",bg='yellow', fg='black', command = ViewBook)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.08)
    
btn4 = Button(root,text="Issue Book",bg='green', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.08)
    
btn5 = Button(root,text="View Issued Book",bg='blue', fg='white', command = ViewIssue)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.08)

root.mainloop()

