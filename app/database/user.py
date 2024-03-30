from shared import db


class User(db.Model):
    user_id = db.Column("uid",db.Integer, primary_key = True)
    username = db.Column("name",db.String(50), unique = True, nullable = False)
    email = db.Column("email",db.String(50), nullable= False)
    password = db.Column("pass",db.String(50), nullable = False)
    
    def __init__(self, uid, name, email, password):
         self.user_id = uid
         self.username = name
         self.email = email
         self.password = password
        