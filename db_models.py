from server import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, nullable = False)
    password = db.Column(db.String(120), nullable = False)

    def __repr__(self):
        return f"User(id='{self.id}' username='{self.username}' password='{self.password}')"