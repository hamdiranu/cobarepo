from blueprints import db
from flask_restful import fields
import datetime

class InternalBooks(db.Model):
    __tablename__= "InternalBook"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    isbn = db.Column(db.String(100), unique = True, nullable = False)
    title = db.Column(db.String(200), nullable = False)
    pengarang = db.Column(db.String(100))
    penerbit = db.Column(db.String(100), nullable = False)
    harga = db.Column(db.Integer, nullable = True, default=20)
    status = db.Column(db.String(100), nullable = False)
    client_id = db.Column(db.Integer, db.ForeignKey("Client.id"), nullable = False)
    url_picture = db.Column(db.String(100), nullable = True)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate = datetime.datetime.now())
    deleted = db.Column(db.Boolean, default = False)

    response_fields = {
        'id'           : fields.Integer,
        'isbn'         : fields.String,
        'title'        : fields.String,
        'pengarang'    : fields.String,
        'penerbit'     : fields.String,
        'harga'        : fields.Integer,
        'status'       : fields.String,
        'client_id'    : fields.Integer
    }

    def __init__(self, isbn, title, pengarang, penerbit, harga, status, client_id):
        self.isbn = isbn
        self.title = title
        self.pengarang = pengarang
        self.penerbit = penerbit
        self.harga  = harga
        self.status = status
        self.client_id = client_id

    def __repr_(self):
        return '<InternalBook %r>' %self.id