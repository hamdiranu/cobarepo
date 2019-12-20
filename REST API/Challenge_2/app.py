# app.py

from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

from blueprints.User.resource import bp_user

######################
#  Import Blueprint  #
######################

app.register_blueprint(bp_user, url_prefix = '/user')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)