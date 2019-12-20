from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.InternalBook.model import InternalBooks
from blueprints.Client.model import Clients
from blueprints.PublicBuku.model import PublicBukus

from blueprints import db,app

bp_publicBuku = Blueprint('publicBuku', __name__)
api = Api(bp_publicBuku)


################################################
#              USING RESTFUL-API               #  
################################################

class PublicBukuList(Resource):

    def __init__(self):
        pass
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', location = 'args', type = int, default = 1)
        parser.add_argument('total_page', location = 'args', type = int, default = 25)
        parser.add_argument('per_page', location = 'args', type = int, default = 25)
        
        args = parser.parse_args()

        qry = InternalBooks.query
        qry2 = {}
        qry2['page'] = args['page']
        qry2['total_page'] = args['total_page']
        qry2['per_page'] = args['per_page']

        listbook = []

        for data in qry:
            
            claims = get_jwt_claims()
            if claims['isinternal'] == True:
                return {'status': 'FORBIDDEN', 'message': 'Non-Internal Only!'}, 403
            
            marshalBuku = marshal(data, InternalBooks.response_fields)

            if marshalBuku['status']=="show":
                listbook.append(marshalBuku)
            
        qry2["data"] = listbook

        return qry2, 200, {'Content-Type' : 'application/json' }

api.add_resource(PublicBukuList, '', '/list')