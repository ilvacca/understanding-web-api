import sqlite3

DBPATH = "10/data/db.db"

def connectToDB():
    db = sqlite3.connect(DBPATH)
    cursor = db.cursor()
    return(db, cursor)

def closeDB(db, cursor):
    cursor.close()
    db.close()

def getAll():
    db, cursor = connectToDB()
    query = "SELECT * FROM users;"
    result = cursor.execute(query)
    rawOutput = result.fetchall()
    closeDB(db, cursor)
    output = []
    for element in rawOutput:
        tempDict = {}
        tempDict["id"] = element[0]
        tempDict["name"] = element[1]
        tempDict["age"] = element[2]
        output.append(tempDict)
    return(output)

def addUserToDB(id, name, age):
    print("Trying inserting USER: [%s, %s, %s] in the DB" % (id, name, age))
    db, cursor = connectToDB()
    query = "INSERT INTO users (id, name, age) VALUES (%s, '%s', %s);" % (id, name, age)
    cursor.execute(query)
    db.commit()
    closeDB(db, cursor)
    print("Inserted %s in the DB" % name)
    return(True)