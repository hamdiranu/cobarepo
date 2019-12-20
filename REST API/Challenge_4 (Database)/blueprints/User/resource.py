from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from .model import Users

from blueprints import db,app

from blueprints.Client.model import Clients

bp_user = Blueprint('user', __name__)
api = Api(bp_user)


################################################
#              USING RESTFUL-API               #  
################################################


class UserResource(Resource):

    def __init__(self):
        pass

    def get(self, id):
        qry = Users.query.get(id)
        if qry is not None and qry.deleted == False:
            return marshal(qry, Users.response_fields), 200
        return {'status':'NOT_FOUND'}, 404

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('name', location = 'json', required = True)
        parser.add_argument('age', location = 'json', type = int, required = True)
        parser.add_argument('sex', location = 'json')
        parser.add_argument('client_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        user = Users(args['name'], args['age'], args['sex'], args['client_id'])
        db.session.add(user)
        db.session.commit()

        app.logger.debug('DEBUG : %s', user)

        return marshal(user, Users.response_fields), 200, {'Content-Type' : 'application/json' }
    
    def put(self, id):

        parser = reqparse.RequestParser()
        parser.add_argument('name', location = 'json', required = True)
        parser.add_argument('age', location = 'json', type = int, required = True)
        parser.add_argument('sex', location = 'json')
        parser.add_argument('client_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        qry = Users.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.name = args['name']
        qry.age = args['age']
        qry.sex = args['sex']
        db.session.commit()

        return marshal(qry, Users.response_fields), 200, {'Content-Type' : 'application/json' }

    def delete(self,id):
        qry = Users.query.get(id)

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

class UserList(Resource):

    def __init__(self):
        pass

    def get(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location = 'args', type = int, default = 1)
        parser.add_argument('rp', location = 'args', type = int, default = 25)
        parser.add_argument('sex', location = 'args', help = 'invalid sort value', choices = ('male','female'))
        parser.add_argument('orderby', location = 'args', help = 'invalid sort value', choices = ('age','sex'))
        parser.add_argument('sort', location = 'args', help = 'invalid sort value', choices = ('desc','asc'))
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Users.query

        # qry = Users.query.filter(Users.name.like("%"+args['name']+"%"))

        if args['sex'] is not None:
            qry = qry.filter_by(sex = args['sex'])

        if args['orderby'] is not None :
            if args['orderby'] == 'age':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.age))
                else:
                    qry = qry.order_by(Users.age)
            elif args['orderby'] == 'sex':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Users.sex))
                else:
                    qry = qry.order_by(Users.sex)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            if row is not None and row.deleted == False:
                rows.append(marshal(row,Users.response_fields))
        return rows, 200

api.add_resource(UserList, '', '/list')
api.add_resource(UserResource, '', '/<id>')
