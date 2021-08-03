import sqlite3
from tkinter import *
from Database import DatabaseManager

database = DatabaseManager("crime.db")

root = Tk()

def initialise():
    database.ShowTables()

    root.geometry("1200x1000")
    root.title("Offence Numbers Database")
    root.withdraw()

    login()

def login():
    loginWindow = Toplevel(root)
    loginWindow.title("Login")
    loginWindow.geometry("375x150")
    loginWindow.grid_rowconfigure(0, weight=1)
    loginWindow.grid_columnconfigure(0, weight=1)

    loginFrame = LabelFrame(loginWindow, text = "Login", padx = 5, pady = 5)
    loginFrame.grid(column = 0, row = 0, padx = 5)

    emailText = Label(loginFrame, text = "Email: ", font = ("Arial", 15), fg = "black")
    emailText.grid(column = 0, row = 0)
    emailEntry = Entry(loginFrame, width = 40)
    emailEntry.grid(column = 1, row = 0)
    passText = Label(loginFrame, text = "Password: ", font = ("Arial", 15), fg = "black")
    passText.grid(column = 0, row = 1)
    passEntry = Entry(loginFrame, show="*", width = 40)
    passEntry.grid(column = 1, row = 1)

    loginButton = Button(loginFrame, text = "Login", width = 15, height = 2, command = lambda: database.CheckCredentials(userEntry.get(), passEntry.get()))
    loginButton.grid(column = 1, row = 2)

def MainWindow():
    root.deiconify()

    navigationFrame = LabelFrame(root, text = "Navigation", padx = 5, pady = 5)
    navigationFrame.grid(column = 0, row = 0, padx = 5)

if __name__ == "__main__":
    initialise()
    root.mainloop()