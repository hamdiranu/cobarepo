from flask import Blueprint
from flask_restful import Api, reqparse, marshal, Resource, inputs
from sqlalchemy import desc
from . import *
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.InternalBook.model import InternalBooks
from blueprints.Client.model import Clients
from blueprints.PenerbitBuku.model import PenerbitBukus

from blueprints import db,app

bp_penerbitBuku = Blueprint('penerbitBuku', __name__)
api = Api(bp_penerbitBuku)


################################################
#              USING RESTFUL-API               #  
################################################


class PenerbitBukuResource(Resource):

    def __init__(self):
        pass

    @jwt_required
    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('isbn', location = 'json', required = True)
        parser.add_argument('title', location = 'json', required = True)
        parser.add_argument('penerbit', location = 'json', required = True)
        parser.add_argument('harga', location = 'json', type = int, required = True)
        args = parser.parse_args()

        penerbitbuku = PenerbitBukus(args['isbn'], args['title'], args['penerbit'], args['harga'])
        db.session.add(penerbitbuku)
        db.session.commit()

        app.logger.debug('DEBUG : %s', penerbitbuku)

        return marshal(penerbitbuku, PenerbitBukus.response_fields), 200, {'Content-Type' : 'application/json' }

class PenerbitBukuList(Resource):

    def __init__(self):
        pass
    
    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', location = 'args', type = int, default = 1)
        parser.add_argument('rp', location = 'args', type = int, default = 25)
        
        args = parser.parse_args()

        offset = (args['p'] * args['rp']) - args['rp']

        qry = InternalBooks.query
        qry2 = PenerbitBukus.query
        
        marshalpenerbitbuku= marshal(qry2, PenerbitBukus.response_fields)

        listbook=[]

        for data in qry:
            
            claims = get_jwt_claims()
            if claims['isinternal'] == True:
                return {'status': 'FORBIDDEN', 'message': 'Non-Internal Only!'}, 403
            qry2 = Clients.query.filter_by(client_key = claims['client_key'])
            clientData = qry2.first()
            
            qry_buku = InternalBooks.query.get(claims.id)
            marshalBuku = marshal(qry_buku, InternalBooks.response_fields)

            if marshalBuku['client_id']==claims.id:
                listbook.append(marshalBuku)
            
        marshalpenerbitbuku["data"] = listbook

        return marshalpenerbitbuku, 200, {'Content-Type' : 'application/json' }

api.add_resource(PenerbitBukuList, '', '/list')
api.add_resource(PenerbitBukuResource, '', '/<id>')