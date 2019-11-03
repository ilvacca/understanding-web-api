from flask import Flask, jsonify, request
import json
import pandas as pd

app = Flask(__name__)

myDataframe = pd.read_csv("8/data.txt", sep="\t", dtype="object")

@app.route('/')
def index():
    pageTitle = "<h1>Title</h1>"
    pageContent = "<p>This is a paragraph</p>"
    completePage = pageTitle + pageContent
    return(completePage)

@app.route('/api')
def allUsers():
    output = [row.to_dict() for _,row in myDataframe.iterrows()]
    return(jsonify(output))

@app.route("/api/user")
def userById():
    arguments = request.args
    id = str(arguments["id"])
    row = myDataframe[myDataframe["id"] == id]
    result = [row.iloc[0].to_dict()]
    return(jsonify(result))

if __name__ == "__main__":
	app.run()