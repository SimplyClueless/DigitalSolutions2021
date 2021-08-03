from deviceFunctions import Database

#Connects to the online server location
db = Database("35.201.1.208", "root", "Sheldon#1")

# Creates the actual database file
query = "CREATE DATABASE benHealthService"
db.ReturnData(query)
db.Commit()

# Creats a table with the defined variables
query = """CREATE TABLE carerDetails (
    carerID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    emailAddress varchar(255) NOT NULL UNIQUE,
    password varchar(255) NOT NULL
    )"""
db.ReturnData(query)
db.Commit()

query = """CREATE TABLE patientData (
    patientID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    carerID int NOT NULL,
    deviceID varchar(255) NOT NULL,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    emailAddress varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    emergencyPhone varchar(255) NOT NULL,
    dob varchar(255) NOT NULL,
    gender varchar(255) NOT NULL,
    address varchar(255) NOT NULL,
    healthConditions varchar(255) NOT NULL
    )"""
db ReturnData(query)
db.Commit()

query = """CREATE TABLE deviceInformation(
    deviceID varchar(255) NOT NULL,
    heartRate int NOT NULL,
    acceleration float NOT NULL,
    temperature float NOT NULL,
    dateTime DateTime Default Current_Timestamp
    )"""
db ReturnData(query)
db.Commit()

db.Close()
