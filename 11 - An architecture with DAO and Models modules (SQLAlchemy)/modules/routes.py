from flask import current_app as app
from flask import request, jsonify, request
from modules.dao import DAO

dao = DAO()

@app.route('/')
def index():
    page = "<h1>Welcome</h1><p>This is a website!</p>"
    return(page)

@app.route("/api")
def api():
    page = "<h1>API</h1><p>Please read the API documentation.</p>"
    return(page)

@app.route("/api/users")
def getUsers():
    queryResult = dao.getAllUsersFromDB()
    output = [user.to_dict() for user in queryResult]
    response = jsonify(output)
    return(response)

@app.route("/api/user")
def getUserById():
    id = request.args["id"]
    queryResult = dao.getUserById(id)
    output = [user.to_dict() for user in queryResult]
    response = jsonify(output)
    return(response)

@app.route("/api/newUser")
def newUser():
    arguments = request.args
    id = arguments["id"] if "id" in list(arguments.keys()) else None
    name = arguments["name"] if "name" in list(arguments.keys()) else None
    age = arguments["age"] if "age" in list(arguments.keys()) else None
    if (id != None) & (name != None) & (age != None):
        dao.addUserToDB(id, name, age)
        return("<h1>User inserted in the DB :)</h1>")
    else:
        return("<h1>User not inserted in the DB :(</h1><p>Please specificate proper arguments (id, name, age)</p>")
    