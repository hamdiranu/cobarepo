from blueprints import db
from flask_restful import fields
import datetime

class PublicBukus(db.Model):
    __tablename__= "PublicBuku"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    page = db.Column(db.Integer, nullable = False, default=1)
    total_page = db.Column(db.Integer, nullable = False, default=1)
    per_page = db.Column(db.Integer, nullable = False, default=25)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate = datetime.datetime.now())
    deleted = db.Column(db.Boolean, default = False)

    response_fields = {
        'page'           : fields.Integer,
        'total_page'     : fields.Integer,
        'per_page'       : fields.Integer
        }

    def __init__(self):
        pass

    def __repr_(self):
        return '<PublicBuku %r>' %self.id