from blueprints import db
from flask_restful import fields
import datetime

class PenerbitBukus(db.Model):
    __tablename__= "PenerbitBuku"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    isbn = db.Column(db.String(100), unique = True, nullable = False)
    title = db.Column(db.String(200), nullable = False)
    penerbit = db.Column(db.String(100), nullable = False)
    harga = db.Column(db.Integer, nullable = False, default=20)
    client_id = db.Column(db.Integer, db.ForeignKey("Client.id"), nullable = False)
    page = db.Column(db.Integer, nullable = False, default=1)
    total_page = db.Column(db.Integer, nullable = False, default=1)
    per_page = db.Column(db.Integer, nullable = False, default=25)
    return_date = db.Column(db.DateTime, default = datetime.datetime.now()+datetime.timedelta(days=4))
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate = datetime.datetime.now())
    deleted = db.Column(db.Boolean, default = False)

    response_fields = {
        'page'           : fields.Integer,
        'total_page'     : fields.Integer,
        'per_page'       : fields.Integer
        }

    def __init__(self, isbn, title, penerbit, harga):
        self.isbn = isbn
        self.title = title
        self.penerbit = penerbit
        self.harga = harga

    def __repr_(self):
        return '<PenerbitBuku %r>' %self.id