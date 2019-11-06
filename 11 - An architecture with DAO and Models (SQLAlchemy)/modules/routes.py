from flask import current_app as app
from flask import jsonify
from modules.models import db, Users

@app.route('/')
def index():
    response = Users.query.all()[0]
    return(jsonify(response))