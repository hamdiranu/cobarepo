from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from .model import Books

from blueprints import db,app

bp_book = Blueprint('book', __name__)
api = Api(bp_book)


################################################
#              USING RESTFUL-API               #  
################################################


class BookResource(Resource):

    def __init__(self):
        pass

    def get(self, id):
        qry = Books.query.get(id)
        if qry is not None and qry.deleted == False:
            return marshal(qry, Books.response_fields), 200
        return {'status':'NOT_FOUND'}, 404

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('title', location = 'json', required = True)
        parser.add_argument('isbn', location = 'json', required = True)
        parser.add_argument('writer', location = 'json')
        args = parser.parse_args()

        book = Books(args['title'], args['isbn'], args['writer'])
        db.session.add(book)
        db.session.commit()

        app.logger.debug('DEBUG : %s', book)

        return marshal(book, Books.response_fields), 200, {'Content-Type' : 'application/json' }
    
    def put(self, id):

        parser = reqparse.RequestParser()
        parser.add_argument('title', location = 'json', required = True)
        parser.add_argument('isbn', location = 'json', required = True)
        parser.add_argument('writer', location = 'json')
        args = parser.parse_args()

        qry = Books.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.title = args['title']
        qry.isbn = args['isbn']
        qry.writer = args['writer']
        db.session.commit()

        return marshal(qry, Books.response_fields), 200, {'Content-Type' : 'application/json' }

    def delete(self,id):
        qry = Books.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        # Hard Delete
        # db.session.delete(qry)
        # db.session.commit()

        # Soft Delete
        qry.deleted = True
        db.session.commit()
        return {'status':'Deleted'}, 200

    def patch(self):
        return 'Not yet implement', 501

class BookList(Resource):

    def __init__(self):
        pass

    def get(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location = 'args', type = int, default = 1)
        parser.add_argument('rp', location = 'args', type = int, default = 25)
        parser.add_argument('writer', location = 'args')
        parser.add_argument('orderby', location = 'args', help = 'invalid sort value', choices = ('writer'))
        parser.add_argument('sort', location = 'args', help = 'invalid sort value', choices = ('desc','asc'))
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Books.query

        # qry = Books.query.filter(Books.title.like("%"+args['title']+"%"))

        if args['writer'] is not None:
            qry = qry.filter_by(writer = args['writer'])

        if args['orderby'] is not None :
            if args['orderby'] == 'writer':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Books.writer))
                else:
                    qry = qry.order_by(Books.writer)
        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            if row is not None and row.deleted == False:
                rows.append(marshal(row,Books.response_fields))
        return rows, 200

api.add_resource(BookList, '', '/list')
api.add_resource(BookResource, '', '/<id>')