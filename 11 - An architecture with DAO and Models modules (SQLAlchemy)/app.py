from flask import Flask

if __name__ == "__main__":
    
    app = Flask(__name__)

    with app.app_context():
        import modules.routes
        app.run()
