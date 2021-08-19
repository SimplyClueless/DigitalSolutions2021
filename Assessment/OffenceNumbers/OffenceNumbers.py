import sqlite3
import os
from tkinter import *
from tkinter import ttk
from Database import DatabaseManager

baseDir = os.path.dirname(os.path.abspath(__file__))
dbPath = os.path.join(baseDir, "crime.db")
database = DatabaseManager(dbPath)
imagePath = os.path.join(baseDir, "graph.png")

root = Tk()
loginWindow = Toplevel(root)
registerWindow = Toplevel(root)
rawFrame = LabelFrame(root, text = "Raw Data")
graphFrame = LabelFrame(root, text = "Graph Data")
importFrame = LabelFrame(root, text = "Import Crime")
officerRegisterFrame = LabelFrame(root, text = "Register Officer")

def initialise():
    root.geometry("1200x900")
    root.title("Offence Numbers Database")
    root.withdraw()

    Login()

def Login():
    loginWindow.deiconify()
    registerWindow.withdraw()

    loginWindow.title("Login")
    loginWindow.geometry("410x270")
    loginWindow.grid_rowconfigure(0, weight=1)
    loginWindow.grid_columnconfigure(0, weight=1)
    loginFrame = LabelFrame(loginWindow, text = "Login", padx = 5, pady = 5)
    loginFrame.pack(padx = 5, pady = 5)

    emailText = Label(loginFrame, text = "Email Address: ", font = ("Arial", 15), fg = "black")
    emailText.grid(column = 0, row = 0)
    emailEntry = Entry(loginFrame, width = 30)
    emailEntry.grid(column = 1, row = 0)
    passText = Label(loginFrame, text = "Password: ", font = ("Arial", 15), fg = "black")
    passText.grid(column = 0, row = 1)
    passEntry = Entry(loginFrame, show="*", width = 30)
    passEntry.grid(column = 1, row = 1)

    loginButton = Button(loginFrame, text = "Login", width = 20, height = 4, command = lambda: CheckLogin(emailEntry.get(), passEntry.get()))
    loginButton.grid(column = 1, row = 2, padx = 10, pady = 10)
    registerText = Label(loginFrame, text = "Not a user? Register Now!", font = ("Arial", 12), fg = "black")
    registerText.grid(column = 0, row = 3)
    registerButton = Button(loginFrame, text = "Register", width = 20, height = 4, command = CivilianRegister)
    registerButton.grid(column = 1, row = 3, padx = 10, pady = 10)

def CheckLogin(email, password):
    credentialCheck = database.CheckCredentials(email, password)
    if credentialCheck != "Error":
        #MainWindow(credentialCheck)
        MainWindow("PoliceHR")
    else:
        print("Error")

def CivilianRegister():
    registerWindow.deiconify()
    loginWindow.withdraw()

    registerWindow.title("Register")
    registerWindow.geometry("415x250")
    registerWindow.grid_rowconfigure(0, weight=1)
    registerWindow.grid_columnconfigure(0, weight=1)
    registerFrame = LabelFrame(registerWindow, text = "Register", padx = 5, pady = 5)
    registerFrame.pack(padx = 5, pady = 5)

    firstNameText = Label(registerFrame, text = "First Name: ", font = ("Arial", 15), fg = "black")
    firstNameText.grid(column = 0, row = 0)
    firstNameEntry = Entry(registerFrame, width = 40)
    firstNameEntry.grid(column = 1, row = 0)
    lastNameText = Label(registerFrame, text = "Last Name: ", font = ("Arial", 15), fg = "black")
    lastNameText.grid(column = 0, row = 1)
    lastNameEntry = Entry(registerFrame, width = 40)
    lastNameEntry.grid(column = 1, row = 1)
    emailText = Label(registerFrame, text = "Email Address: ", font = ("Arial", 15), fg = "black")
    emailText.grid(column = 0, row = 2)
    emailEntry = Entry(registerFrame, width = 40)
    emailEntry.grid(column = 1, row = 2)
    passText = Label(registerFrame, text = "Password: ", font = ("Arial", 15), fg = "black")
    passText.grid(column = 0, row = 3)
    passEntry = Entry(registerFrame, show="*", width = 40)
    passEntry.grid(column = 1, row = 3)

    registerUserButton = Button(registerFrame, text = "Register User", width = 20, height = 4, command = lambda: CheckCivilianRegister(firstNameEntry.get(), lastNameEntry.get(), emailEntry.get(), passEntry.get()))
    registerUserButton.grid(column = 1, row = 4, padx = 10, pady = 10)
    returnButton = Button(registerFrame, text = "Back to Login", width = 20, height = 4, command = Login)
    returnButton.grid(column = 0, row = 4, padx = 10, pady = 10)

def CheckCivilianRegister(firstName, lastName, email, password):
    if database.RegisterCivilian(firstName, lastName, email, password):
        registerWindow.withdraw()
        loginWindow.deiconify()

def FrameManager():
    rawFrame.pack_forget()
    graphFrame.pack_forget()
    importFrame.pack_forget()
    officerRegisterFrame.pack_forget()

def DisplayRawData():
    FrameManager()
    rawFrame.pack(padx = 5, pady = 5, expand = True, fill = "both", side = "right")
    tree = ttk.Treeview(rawFrame, column=("c1", "c2", "c3", "c4", "c5"), show="headings")
    tree.pack_forget()
    tree.column("#1", anchor=CENTER); tree.heading("#1", text="District")
    tree.column("#2", anchor=CENTER); tree.heading("#2", text="Month & Year")
    tree.column("#3", anchor=CENTER); tree.heading("#3", text="Offences Against Persons")
    tree.column("#4", anchor=CENTER); tree.heading("#4", text="Offences Against Property")
    tree.column("#5", anchor=CENTER); tree.heading("#5", text="Other Offences")
    data = database.ReturnData()
    rows = data.fetchall()
    for row in rows:
        tree.insert("", END, values=row)
    tree.pack(padx = 5, pady = 5, expand = True, fill = "y")

def DisplayGraphData():
    FrameManager()
    graphFrame.pack(padx = 5, pady = 5, expand = True, fill = "both", side = "right")
    test = PhotoImage(imagePath)
    image = Label()

def DisplayImportCrime():
    FrameManager()
    importFrame.pack(padx = 5, pady = 5, expand = True, fill = "both", side = "right")

def DisplayRegisterOfficer():
    FrameManager()
    officerRegisterFrame.pack(padx = 5, pady = 5, expand = True, fill = "both", side = "right")

def CheckOfficerRegister(firstName, lastName, email, password, year, month, day, rank, region):
    dob = year + month[:2] + day
    database.RegisterOfficer(firstName, lastName, email, password, dob, rank, region)

def MainWindow(userType):
    root.deiconify()
    loginWindow.withdraw()

    # Window frame setup
    navigationFrame = LabelFrame(root, text = "Navigation")
    navigationFrame.pack(padx = 5, pady = 5, expand = True, fill = "y", anchor = "w", side = "left")
    DisplayRawData()

    # Navigation Buttons
    rawButton = Button(navigationFrame, text = "Raw Data", width = 20, height = 4, command = DisplayRawData)
    rawButton.grid(column = 0, row = 0, padx = 10, pady = 10)
    graphButton = Button(navigationFrame, text = "Graph Data", width = 20, height = 4, command = DisplayGraphData)
    graphButton.grid(column = 0, row = 1, padx = 10, pady = 10)

    if (userType == "PoliceLR"):
        importButton = Button(navigationFrame, text = "Import Crime", width = 20, height = 4, command = DisplayImportCrime)
        importButton.grid(column = 0, row = 2, padx = 10, pady = 10)
    elif (userType == "PoliceHR"):
        importButton = Button(navigationFrame, text = "Import Crime", width = 20, height = 4, command = DisplayImportCrime)
        importButton.grid(column = 0, row = 2, padx = 10, pady = 10)
        registerButton = Button(navigationFrame, text = "Register Officer", width = 20, height = 4, command = DisplayRegisterOfficer)
        registerButton.grid(column = 0, row = 3, padx = 10, pady = 10)

    # Register Officer
    firstNameLabel = Label(officerRegisterFrame, text = "First Name: ", font = ("Arial", 15), fg = "black")
    firstNameLabel.grid(column = 0, row = 0, padx = 5, pady = 5)
    firstNameEntry = Entry(officerRegisterFrame, width = 40)
    firstNameEntry.grid(column = 1, row = 0, padx = 5, pady = 5, columnspan = 6, sticky = "w")
    lastNameLabel = Label(officerRegisterFrame, text = "Last Name: ", font = ("Arial", 15), fg = "black")
    lastNameLabel.grid(column = 0, row = 1, padx = 5, pady = 5)
    lastNameEntry = Entry(officerRegisterFrame, width = 40)
    lastNameEntry.grid(column = 1, row = 1, padx = 5, pady = 5, columnspan = 6, sticky = "w")
    emailLabel = Label(officerRegisterFrame, text = "Email Address: ", font = ("Arial", 15), fg = "black")
    emailLabel.grid(column = 0, row = 2, padx = 5, pady = 5)
    emailEntry = Entry(officerRegisterFrame, width = 40)
    emailEntry.grid(column = 1, row = 2 ,padx = 5, pady = 5, columnspan = 6, sticky = "w")
    passwordLabel = Label(officerRegisterFrame, text = "Password: ", font = ("Arial", 15), fg = "black")
    passwordLabel.grid(column = 0, row = 3, padx = 5, pady = 5)
    passwordEntry = Entry(officerRegisterFrame, show="*", width = 40)
    passwordEntry.grid(column = 1, row = 3, padx = 5, pady = 5, columnspan = 6, sticky = "w")
 
    dobLabel = Label(officerRegisterFrame, text = "Date of Birth: ", font = ("Arial", 15), fg = "black")
    dobLabel.grid(column = 0, row = 4, padx = 5, pady = 5)
    yearLabel = Label(officerRegisterFrame, text = "Year: ", font = ("Arial", 15), fg = "black")
    yearLabel.grid(column = 1, row = 4, padx = 5, pady = 5)
    yearDropdown = ttk.Combobox(officerRegisterFrame)
    years = []
    for year in range (1900, 2022, 1):
        years.append(year)
    years.reverse()
    yearDropdown['values'] = years
    yearDropdown.grid(column = 2, row = 4, padx = 5, pady = 5)
    monthLabel = Label(officerRegisterFrame, text = "Month: ", font = ("Arial", 15), fg = "black")
    monthLabel.grid(column = 3, row = 4, padx = 5, pady = 5)
    monthDropdown = ttk.Combobox(officerRegisterFrame)
    months = ["01 - January", "02 - February", "03 - March", "04 - April", "05 - May", "06 - June", "07 - July", "08 - August", "09 - September", "10 - October", "11 - November", "12 - December"]
    monthDropdown['values'] = months
    monthDropdown.grid(column = 4, row = 4, padx = 5, pady = 5)
    dayLabel = Label(officerRegisterFrame, text = "Day: ", font = ("Arial", 15), fg = "black")
    dayLabel.grid(column = 5, row = 4, padx = 5, pady = 5)
    dayDropdown = ttk.Combobox(officerRegisterFrame)
    days = []
    for day in range (1, 32, 1):
        if len(str(day)) == 1:
            day = "0" + str(day) 
        days.append(day)
    dayDropdown['values'] = days
    dayDropdown.grid(column = 6, row = 4, padx = 5, pady = 5)

    rankLabel = Label(officerRegisterFrame, text = "Rank: ", font = ("Arial", 15), fg = "black")
    rankLabel.grid(column = 0, row = 5, padx = 5, pady = 5)
    rankDropdown = ttk.Combobox(officerRegisterFrame)
    ranks = ["Private"]
    rankDropdown['values'] = ranks
    rankDropdown.grid(column = 1, row = 5, padx = 5, pady = 5)

    regionLabel = Label(officerRegisterFrame, text = "Region: ", font = ("Arial", 15), fg = "black")
    regionLabel.grid(column = 0, row = 6, padx = 5, pady = 5)
    regionDropdown = ttk.Combobox(officerRegisterFrame)
    regions = ["Location"]
    regionDropdown['values'] = regions
    regionDropdown.grid(column = 1, row = 6, padx = 5, pady = 5)

    officerRegisterButton = Button(officerRegisterFrame, text = "Register Officer", width = 20, height = 4, 
        command = lambda: CheckOfficerRegister(firstNameEntry.get(), lastNameEntry.get(), emailEntry.get(), passwordEntry.get(), 
        yearDropdown.get(), monthDropdown.get(), dayDropdown.get(), rankDropdown.get(), regionDropdown.get()))
    officerRegisterButton.grid(column = 0, row = 7, padx = 5, pady = 5)

if __name__ == "__main__":
    initialise()
    root.mainloop()