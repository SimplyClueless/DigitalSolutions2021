import sqlite3

class DatabaseManager:
    def __init__(self, databaseFile):
        self.connection = sqlite3.connect(databaseFile)
        self.cursor = self.connection.cursor()

    def CheckCredentials(self, email, password):
        # Check Civilian Database
        self.cursor.execute(f"SELECT * FROM civilianUsers WHERE emailAddress = ?", [str(email)])
        civilianResults = self.cursor.fetchall()
        if civilianResults != None:
            for user in civilianResults:
                userEmail = user[3]
                self.cursor.execute(f"SELECT password FROM civilianUsers WHERE emailAddress = ?", [str(userEmail)])
                passResults = self.cursor.fetchall()
                for foundPassword in passResults:
                    userPassword = foundPassword[0]
                    # TODO:
                    # Add decrypt function to decrypt stored password before testing against the user inputted password
                    if userPassword == password:
                        return "Civilian"

        # Check Police Database
        self.cursor.execute("SELECT * FROM policeUsers WHERE emailAddress = ?", [str(email)])
        policeResults = self.cursor.fetchall()
        if policeResults != None:
            for userEmail in policeResults:
                self.cursor.execute("SELECT password FROM policeUsers WHERE emailAddress = ?", [str(userEmail)])
                passResults = self.cursor.fetchall()
                for userPassword in passResults:
                    # TODO:
                    # Add decrypt function to decrypt stored password before testing against the user inputted password
                    if userPassword == password:
                        return "Police"

        # If no matching usernames and passwords are found the user cannot login
        print("No user found")
        return "Error"

    def RegisterCivilian(self, firstName, lastName, emailAddress, password):
        # TODO:
        # Add encrypt function to encrypt password before being stored in database
        encryptedPassword = password

        userDetails = (firstName, lastName, emailAddress, encryptedPassword)
        try:
            self.cursor.execute(f"""INSERT INTO civilianUsers (firstName, lastName, emailAddress, password) 
            VALUES (?, ?, ?, ?)""", userDetails)
        except:
            return False
        finally:
            self.connection.commit()
            return True

    def RegisterOfficer(self, firstName, lastName, emailAddress, password, dob, rank, region):
        # TODO
        # Encrypt password before registering user
        pass

    def ReturnData(self):
        return self.cursor.execute("SELECT * FROM districtReportedOffencesNumber")

    def Commit(self):
        self.connection.commit()
        
    def Close(self):
        self.connection.close()