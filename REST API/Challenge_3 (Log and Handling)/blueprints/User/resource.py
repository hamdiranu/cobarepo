from flask import Blueprint
from flask_restful import Api, reqparse, Resource

from . import *

bp_user = Blueprint('user', __name__)
api = Api(bp_user)


################################################
#              USING RESTFUL-API               #  
################################################

class UserResource(Resource):

    users = Users()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location = 'json', required = True)
        parser.add_argument('age', location = 'json', type = int, required = True)
        parser.add_argument('sex', location = 'json')
        parser.add_argument('client_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        user = User()
        user.id = self.users.users[-1]['id']+1
        user.name = args['name']
        user.age = args['age']
        user.sex = args['sex']
        user.client_id = args['client_id']

        self.users.add(user.serialize())
        return user.serialize(), 200, {'Content-Type' : 'application/json' }
    
    def get(self, id=None):
        if id == None:    
            return self.users.get_list(), 200, {'Content-Type' : 'application/json' }
        else :
            output = self.users.get_one_id(id)
            if output is not None:
                return output, 200, {'Content-Type' : 'application/json' }
            else:
                return{'status':'NOT_FOUND', 'message': 'Client not found'}, 404, {'Content-Type' : 'application/json' }

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', location = 'json', required = True)
        parser.add_argument('age', location = 'json', type = int, required = True)
        parser.add_argument('sex', location = 'json')
        parser.add_argument('client_id', location = 'json', type = int, required = True)
        args = parser.parse_args()

        user = User()
        user.id = id
        user.name = args['name']
        user.age = args['age']
        user.sex = args['sex']
        user.client_id = args['client_id']

        self.users.edit_data(id, user.name, user.age, user.sex, user.client_id)
        return user.serialize(), 200, {'Content-Type' : 'application/json' }

    def delete(self,id):
        self.users.delete(id)
        return 'Deleted', 200

    def patch(self):
        return 'Not yet implement', 501

api.add_resource(UserResource, '', '/<id>')