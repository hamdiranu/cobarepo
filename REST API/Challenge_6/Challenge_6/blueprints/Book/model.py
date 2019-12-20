from blueprints import db
from flask_restful import fields
import datetime

class Books(db.Model):
    __tablename__= "Book"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(30), unique = True, nullable = False)
    isbn = db.Column(db.String(50), nullable = True)
    writer = db.Column(db.String(10), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.datetime.now())
    update_at = db.Column(db.DateTime, onupdate = datetime.datetime.now())
    deleted = db.Column(db.Boolean, default = False)

    response_fields = {
        'created_at'   : fields.DateTime,
        'updated_at'   : fields.DateTime,
        'deleted'      : fields.Boolean,
        'id'           : fields.Integer,
        'title'        : fields.String,
        'isbn'         : fields.String,
        'writer'       : fields.String
    }

    def __init__(self, title, isbn, writer):
        self.title = title
        self.isbn = isbn
        self.writer = writer

    def __repr_(self):
        return '<Book %r>' %self.id