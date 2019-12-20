from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from .model import Rents
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.User.model import Users
from blueprints.Book.model import Books
from blueprints.Client.model import Clients

from blueprints import db,app

bp_rent = Blueprint('rent', __name__)
api = Api(bp_rent)


################################################
#              USING RESTFUL-API               #  
################################################


class RentResource(Resource):

    def __init__(self):
        pass

    @jwt_required
    def get(self, id):
        qry = Rents.query.get(id)

        claims = get_jwt_claims()
        if claims['isinternal'] == True:
            return {'status': 'FORBIDDEN', 'message': 'Non-Internal Only!'}, 403
        qry2 = Clients.query.filter_by(client_key = claims['client_key'])
        clientData = qry2.first()

        if qry is None or qry.deleted == True:
            return {'status':'NOT_FOUND'}, 404, {'Content-Type' : 'application/json' }
        marshalRents = marshal(qry, Rents.response_fields)

        qry_user = Users.query.get(marshalRents["user_id"])
        marshalUser = marshal(qry_user, Users.response_fields)
        qry_book = Books.query.get(marshalRents["book_id"])
        marshalBook = marshal(qry_book, Books.response_fields)

        marshalRents["user"] = marshalUser
        marshalRents["book"] = marshalBook
        
        if marshalRents["user"]["client_id"] == clientData.id:
            return marshalRents, 200, {'Content-Type' : 'application/json' }

    @jwt_required
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('book_id', location = 'json', type = int, required = True)
        parser.add_argument('user_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        rent = Rents(args['book_id'], args['user_id'])
        db.session.add(rent)
        db.session.commit()

        app.logger.debug('DEBUG : %s', rent)

        return marshal(rent, Rents.response_fields), 200, {'Content-Type' : 'application/json' }

    @jwt_required
    def delete(self,id):
        qry = Rents.query.get(id)

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
    def patch(self):
        return 'Not yet implement', 501

class RentList(Resource):

    def __init__(self):
        pass
    
    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location = 'args', type = int, default = 1)
        parser.add_argument('rp', location = 'args', type = int, default = 25)
        parser.add_argument('book_id', location = 'args')
        parser.add_argument('user_id', location = 'args')
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Rents.query

        if args['book_id'] is not None:
            qry = qry.filter_by(book_id = args['book_id'])

        if args['user_id'] is not None:
            qry = qry.filter_by(user_id = args['user_id'])
        
        result = []
        for data in qry:
            
            claims = get_jwt_claims()
            if claims['isinternal'] == True:
                return {'status': 'FORBIDDEN', 'message': 'Non-Internal Only!'}, 403
            qry2 = Clients.query.filter_by(client_key = claims['client_key'])
            clientData = qry2.first()
            
            marshalRents = marshal(data, Rents.response_fields)

            qry_user = Users.query.get(marshalRents["user_id"])
            marshalUser = marshal(qry_user, Users.response_fields)
            qry_book = Books.query.get(marshalRents["book_id"])
            marshalBook = marshal(qry_book, Books.response_fields)

            marshalRents["user"] = marshalUser
            marshalRents["book"] = marshalBook

            if marshalRents["user"]["client_id"] == clientData.id:
                result.append(marshalRents)

        return result, 200, {'Content-Type' : 'application/json' }

api.add_resource(RentList, '', '/list')
api.add_resource(RentResource, '', '/<id>')