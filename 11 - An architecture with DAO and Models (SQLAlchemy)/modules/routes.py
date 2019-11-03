from flask import current_app as app
from modules.models import db, Users

@app.route('/')
def index():
    print("ciao")
    print( Users.query.all()[0])
    return "ciao"