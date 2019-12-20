from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from .model import Rents

from blueprints.User.model import Users
from blueprints.Book.model import Books

from blueprints import db,app

bp_rent = Blueprint('rent', __name__)
api = Api(bp_rent)


################################################
#              USING RESTFUL-API               #  
################################################


class RentResource(Resource):

    def __init__(self):
        pass

    def get(self, id):
        qry = Rents.query.get(id)
        if qry is None or qry.deleted == True:
            return {'status':'NOT_FOUND'}, 404, {'Content-Type' : 'application/json' }
        marshalRents = marshal(qry, Rents.response_fields)

        qry_user = Users.query.get(marshalRents["user_id"])
        marshalUser = marshal(qry_user, Users.response_fields)
        qry_book = Books.query.get(marshalRents["book_id"])
        marshalBook = marshal(qry_book, Books.response_fields)

        marshalRents["user"] = marshalUser
        marshalRents["book"] = marshalBook

        return marshalRents, 200, {'Content-Type' : 'application/json' }

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
    
    def put(self, id):

        parser = reqparse.RequestParser()
        parser.add_argument('book_id', location = 'json', type = int, required = True)
        parser.add_argument('user_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        qry = Rents.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.book_id = args['book_id']
        qry.user_id = args['user_id']
        db.session.commit()

        return marshal(qry, Rents.response_fields), 200, {'Content-Type' : 'application/json' }

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

    def patch(self):
        return 'Not yet implement', 501

class RentList(Resource):

    def __init__(self):
        pass

    def get(self):
        qry = Rents.query.all()

        result = []
        for data in qry:
            marshalRents = marshal(data, Rents.response_fields)

            qry_user = Users.query.get(marshalRents["user_id"])
            marshalUser = marshal(qry_user, Users.response_fields)
            qry_book = Books.query.get(marshalRents["book_id"])
            marshalBook = marshal(qry_book, Books.response_fields)

            marshalRents["user"] = marshalUser
            marshalRents["book"] = marshalBook
            result.append(marshalRents)

        if qry is not None:
            return result, 200, {'Content-Type' : 'application/json' }

        else:
            return {'result' : 'ID_NOT_FOUND'}, 404, {'Content-Type' : 'application/json' }

api.add_resource(RentList, '', '/list')
api.add_resource(RentResource, '', '/<id>')