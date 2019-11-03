from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    pageTitle = "HOME"
    pageContent = "Welcome this is the main page"
    return(render_template("myTemplate.html", title=pageTitle, content=pageContent))

@app.route('/blog')
def blog():
    pageTitle = "BLOG"
    pageContent = "This is the blog"
    return(render_template("myTemplate.html", title=pageTitle, content=pageContent))

if __name__ == "__main__":
	app.run()