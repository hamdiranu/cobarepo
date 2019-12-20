from blueprints import db
from flask_restful import fields
import datetime

class Users(db.Model):
    __tablename__= "User"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(30), unique = True, nullable = False)
    age = db.Column(db.Integer, nullable = True, default=20)
    sex = db.Column(db.String(10), nullable = False)
    client_id = db.Column(db.Integer, db.ForeignKey("Client.id"), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate = datetime.datetime.now())
    deleted = db.Column(db.Boolean, default = False)


    response_fields = {
        'id'        : fields.Integer,
        'name'      : fields.String,
        'age'       : fields.Integer,
        'sex'       : fields.String,
        'client_id' : fields.Integer,
        'created_at': fields.DateTime,
        'update_at' : fields.DateTime
    }

    def __init__(self, name, age, sex, client_id):
        self.name = name
        self.age = age
        self.sex = sex
        self.client_id = client_id

    def __repr_(self):
        return '<User %r>' %self.id