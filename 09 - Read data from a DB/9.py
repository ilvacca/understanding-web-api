from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DBPATH = "9/data.db"

@app.route('/')
def index():
    pageTitle = "<h1>Title</h1>"
    pageContent = "<p>This is a paragraph</p>"
    completePage = pageTitle + pageContent
    return(completePage)

@app.route('/api')
def allUsers():
    query = "SELECT * FROM users"
    db = sqlite3.connect(DBPATH)
    cursor = db.cursor()
    result = cursor.execute(query).fetchall()
    db.close()
    columnNames = [col[0].lower() for col in cursor.description]
    output = [dict(zip(columnNames,r)) for r in result]
    return(jsonify(output))

@app.route("/api/user")
def userById():
    arguments = request.args
    id = str(arguments["id"])
    query = "SELECT * FROM users WHERE ID = %s" % id
    db = sqlite3.connect(DBPATH)
    cursor = db.cursor()
    result = cursor.execute(query).fetchall()
    db.close()
    columnNames = [col[0].lower() for col in cursor.description]
    output = [dict(zip(columnNames,r)) for r in result]
    return(jsonify(output))

if __name__ == "__main__":
	app.run()