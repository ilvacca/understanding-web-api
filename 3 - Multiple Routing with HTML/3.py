from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    pageTitle = "<h1>Title</h1>"
    pageContent = "<p>This is a paragraph</p>"
    completePage = pageTitle + pageContent
    return(completePage)

@app.route('/blog')
def blog():
    return("This is the blog")

if __name__ == "__main__":
	app.run()