from deviceFunctions import database

db = database("34.116.119.134", "root", "sheldon1", "benDB")

db.showTables()
db.showVariables("customers")

query = "SELECT * FROM customers"
db.returnData(query)

db.commit()
db.close()