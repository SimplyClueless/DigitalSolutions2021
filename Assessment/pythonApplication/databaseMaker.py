from deviceFunctions import Database

db = Database("35.201.1.208", "root", "Sheldon#1", "benHealthService")

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
    deviceID int NOT NULL,
    firstName varchar(255) NOT NULL,
    lastName varchar(255) NOT NULL,
    emailAddress varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    emergencyPhone varchar(255) NOT NULL
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
