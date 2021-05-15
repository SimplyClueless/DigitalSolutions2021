from deviceFunctions import Database

db = Database("35.201.1.208", "root", "Sheldon#1", "benHealthService")

#query = """CREATE TABLE carerDetails (
#    carerID int PRIMARY KEY NOT NULL AUTO_INCREMENT,
#    firstName varchar(255) NOT NULL,
#    lastName varchar(255) NOT NULL,
#    emailAddress varchar(255) NOT NULL UNIQUE,
#    password varchar(255) NOT NULL
#    )"""

db.DeleteAllData('patientData')
db.Commit()

query = "INSERT INTO patientData (carerID, deviceID, firstName, lastName, emailAddress, password, emergencyPhone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
values = ("9", "1000000054a1de0b", "John", "Doe", "s06442@sheldoncollege.com", "health123!", "0481851721")
db.ImportData(query, values)
db.Commit()

#db.ShowTables()
#db.ShowVariables('patientData')

#db.DeleteAllData('deviceInformation')
#db.Commit()

query = "SELECT * FROM patientData"
db.ReturnData(query)

db.Commit()
db.Close()
