from .server import db

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<Users %r>' % self.name