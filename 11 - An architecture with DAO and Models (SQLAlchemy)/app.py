from modules.server import create_app

app = create_app()

# INSPIRED FROM:
# https://github.com/toddbirchard/flasksqlalchemy-tutorial/blob/master/wsgi.py

if __name__ == "__main__":
    app.run()