from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return("My first website")

@app.route('/blog')
def blog():
    return("This is the blog")

if __name__ == "__main__":
	app.run()


	