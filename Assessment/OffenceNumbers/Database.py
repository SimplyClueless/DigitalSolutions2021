import sqlite3

class DatabaseManager:
    def __init__(self, databaseFile):
        self.connection = sqlite3.connect(databaseFile)
        self.cursor = self.connection.cursor()

    def CheckCredentials(self, email, password):
        self.cursor.execute(f"SELECT * FROM users WHERE username = {email}")
        emailResults = self.cursor.fetchall()
        for userEmail in emailResults:
            self.cursor.execute(f"SELECT * FROM passwords WHERE username = {userEmail}")
            passResults = self.cursor.fetchall()
            for userPassword in passResults:
                if userPassword == password:
                    return True
        return False

    def RegisterCivilian(self):
        pass

    def RegisterOfficer(self, firstName, lastName, emailAddress, password, DOB, rank, region):
        pass

    def Commit(self):
        self.connection.commit()
        
    def Close(self):
        self.connection.close()