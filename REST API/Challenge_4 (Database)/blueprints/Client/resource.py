from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from .model import Clients

from blueprints import db,app

bp_client = Blueprint('client', __name__)
api = Api(bp_client)


################################################
#              USING RESTFUL-API               #  
################################################


class ClientResource(Resource):

    def __init__(self):
        pass

    def get(self, id):
        qry = Clients.query.get(id)
        if qry is not None and qry.deleted == False:
            return marshal(qry, Clients.response_fields), 200
        return {'status':'NOT_FOUND'}, 404

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location = 'json', required = True)
        parser.add_argument('client_secret', location = 'json', required = True)
        parser.add_argument('status', location = 'json')
        args = parser.parse_args()

        client = Clients(args['client_key'], args['client_secret'], args['status'])
        db.session.add(client)
        db.session.commit()

        app.logger.debug('DEBUG : %s', client)

        return marshal(client, Clients.response_fields), 200, {'Content-Type' : 'application/json' }
    
    def put(self, id):

        parser = reqparse.RequestParser()
        parser.add_argument('client_key', location = 'json', required = True)
        parser.add_argument('client_secret', location = 'json', required = True)
        parser.add_argument('status', location = 'json')
        args = parser.parse_args()

        qry = Clients.query.get(id)

        if qry is None:
            return {'status': 'NOT_FOUND'}, 404

        qry.client_key = args['client_key']
        qry.client_secret = args['client_secret']
        qry.status = args['status']
        db.session.commit()

        return marshal(qry, Clients.response_fields), 200, {'Content-Type' : 'application/json' }

    def delete(self,id):
        qry = Clients.query.get(id)

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

class ClientList(Resource):

    def __init__(self):
        pass

    def get(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location = 'args', type = int, default = 1)
        parser.add_argument('rp', location = 'args', type = int, default = 25)
        parser.add_argument('status', location = 'args', help = 'invalid sort value', choices = ('False','True'))
        parser.add_argument('orderby', location = 'args', help = 'invalid sort value', choices = ('status'))
        parser.add_argument('sort', location = 'args', help = 'invalid sort value', choices = ('desc','asc'))
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = Clients.query

        # qry = Clients.query.filter(Clients.client_key.like("%"+args['client_key']+"%"))

        if args['status'] is not None:
            qry = qry.filter_by(status = args['status'])

        if args['orderby'] is not None :
            if args['orderby'] == 'status':
                if args['sort'] == 'desc':
                    qry = qry.order_by(desc(Clients.status))
                else:
                    qry = qry.order_by(Clients.status)

        rows = []
        for row in qry.limit(args['rp']).offset(offset).all():
            if row is not None and row.deleted == False:
                rows.append(marshal(row,Clients.response_fields))
        return rows, 200

api.add_resource(ClientList, '', '/list')
api.add_resource(ClientResource, '', '/<id>')



#join

# class PetWithClient(Resource):

#     def get(self):
#         qry = db.session.query(Pets, Clients).join(Pets.client_id==Clients.id).all()

#         result = []
#         for data in qry:
#             holder = marshal(data[0], Pets.response_field_with_client)
#             holder['username']=data[1].username
#             holder['status'] = data[1].status
#             result.append(holder)

#         if qry is not None:
#             return ("status":"success","reuslt":result), 200, {'Content-Type' : 'application/json' }

#         else:
#             return ("status":"Failed","reuslt":"NOT_FOUND"), 404


# def getall(self):
#     qry = Pets.query.all()

#     result = []
#     for data in qry:
#         marshalPets = marshal(data, Pets.response_fields)

#         qry_client = Client.query.get(marshalPets["client_id"])
#         marshalClient = marshal(qry_client, Clients.response_fields)

#         marshalPets["client"]=marshalClient
#         result.append(marshalPets)

#     if qry is not None:
#         return ("status":"success","reuslt":result), 200, {'Content-Type' : 'application/json' }

#     else:
#         return ("status":"Failed","result":"ID_NOT_FOUND"), 404, {'Content-Type' : 'application/json' }