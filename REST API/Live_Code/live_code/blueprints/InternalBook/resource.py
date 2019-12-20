from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from .model import InternalBooks
from flask_jwt_extended import JWTManager, verify_jwt_in_request, get_jwt_claims, jwt_required
from blueprints import db,app, internal_required

bp_internalBook = Blueprint('internalBook', __name__)
api = Api(bp_internalBook)


################################################
#              USING RESTFUL-API               #  
################################################


class InternalBookResource(Resource):

    def __init__(self):
        pass

    @jwt_required
    @internal_required
    def get(self, id):
        qry = InternalBooks.query.get(id)
        if qry is not None and qry.deleted == False:
            return marshal(qry, InternalBooks.response_fields), 200
        return {'status':'NOT_FOUND'}, 404

    @jwt_required
    @internal_required
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('isbn', location = 'json', required = True)
        parser.add_argument('title', location = 'json', required = True)
        parser.add_argument('pengarang', location = 'json')
        parser.add_argument('penerbit', location = 'json', required = True)
        parser.add_argument('harga', location = 'json', type = int)
        parser.add_argument('status', location = 'json', help = 'invalid sort value', choices = ('show','not_show'))
        parser.add_argument('url_picture', location = 'json')
        parser.add_argument('client_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        internalbook = InternalBooks(args['isbn'], args['title'], args['pengarang'],args['penerbit'],args['harga'],args['status'],args['url_picture'], args['client_id'])
        db.session.add(internalbook)
        db.session.commit()

        app.logger.debug('DEBUG : %s', book)

        return marshal(internalbook, InternalBooks.response_fields), 200, {'Content-Type' : 'application/json' }
    
    @jwt_required
    @internal_required
    def put(self, id):

        parser = reqparse.RequestParser()
        parser.add_argument('isbn', location = 'json', required = True)
        parser.add_argument('title', location = 'json', required = True)
        parser.add_argument('pengarang', location = 'json')
        parser.add_argument('penerbit', location = 'json', required = True)
        parser.add_argument('harga', location = 'json', type = int)
        parser.add_argument('status', location = 'json', help = 'invalid sort value', choices = ('show','not_show'))
        parser.add_argument('url_picture', location = 'json')
        parser.add_argument('client_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        qry = InternalBooks.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.isbn = args['isbn']
        qry.title = args['title']
        qry.pengarang = args['pengarang']
        qry.penerbit = args['penerbit']
        qry.harga = args['harga']
        qry.status = args['status']
        qry.url_picture = args['url_picture']
        qry.client_id = args['client_id']
        db.session.commit()

        return marshal(qry, InternalBooks.response_fields), 200, {'Content-Type' : 'application/json' }

    @jwt_required
    @internal_required
    def delete(self,id):
        qry = InternalBooks.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        # Hard Delete
        # db.session.delete(qry)
        # db.session.commit()

        # Soft Delete
        qry.deleted = True
        db.session.commit()
        return {'status':'Deleted'}, 200

    @jwt_required
    @internal_required
    def patch(self):
        return 'Not yet implement', 501

class InternalBookList(Resource):

    def __init__(self):
        pass
    
    @jwt_required
    @internal_required
    def get(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location = 'args', type = int, default = 1)
        parser.add_argument('rp', location = 'args', type = int, default = 25)
        parser.add_argument('harga', location = 'args')
        parser.add_argument('orderby', location = 'args', help = 'invalid sort value', choices = ('harga'))
        parser.add_argument('sort', location = 'args', help = 'invalid sort value', choices = ('desc','asc'))
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Books.query
        
        if args['harga'] is not None:
            qry = qry.filter_by(harga = args['harga'])

        if args['orderby'] is not None :
            if args['orderby'] == 'harga':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(InternalBooks.harga))
                else:
                    qry = qry.order_by(InternalBooks.harga)
        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            if row is not None and row.deleted == False:
                rows.append(marshal(row,InternalBooks.response_fields))
        return rows, 200

api.add_resource(InternalBookList, '', '/list')
api.add_resource(InternalBookResource, '', '/<id>')