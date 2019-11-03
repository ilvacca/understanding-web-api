from flask import Flask, jsonify

app = Flask(__name__)

myData = [
    {
        "user":"Alessio",
        "age":29
    },{
        "user":"Luca",
        "age":25
    },{
        "user":"Giovanni",
        "age":45
    }
]

@app.route('/')
def index():
    pageTitle = "<h1>Title</h1>"
    pageContent = "<p>This is a paragraph</p>"
    completePage = pageTitle + pageContent
    return(completePage)

@app.route('/welcome/<user>')
def welcome(user):
    completePage = "Hi %s" % (user)
    return(completePage)

@app.route("/api/data")
def api():
    output = jsonify(myData)
    return(output)

if __name__ == "__main__":
	app.run()