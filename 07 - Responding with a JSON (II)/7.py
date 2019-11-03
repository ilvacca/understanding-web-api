from flask import Flask, jsonify, request

app = Flask(__name__)

myData = [
    {
        "id" : 1,
        "user" : "Alessio",
        "age" : 29
    },{
        "id" : 2,
        "user" : "Luca",
        "age" : 25
    },{
        "id" : 3,
        "user" : "Giovanni",
        "age" : 45
    }
]

@app.route('/')
def index():
    pageTitle = "<h1>Title</h1>"
    pageContent = "<p>This is a paragraph</p>"
    completePage = pageTitle + pageContent
    return(completePage)

@app.route('/api')
def allUsers():
    output = jsonify(myData)
    return(output)

@app.route("/api/user")
def userById():
    arguments = request.args
    id = int(arguments["id"])
    queryResult = [element for element in myData if element["id"] == id]
    output = jsonify(queryResult)
    return(output)

if __name__ == "__main__":
	app.run()