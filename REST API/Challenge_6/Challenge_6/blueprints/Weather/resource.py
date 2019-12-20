import requests
from flask import Blueprint
from flask_restful import Api, reqparse, Resource
from flask_jwt_extended import jwt_required

bp_Weather = Blueprint('Weather', __name__)
api = Api(bp_Weather)

class PublicGetCurrentWeather(Resource):

    wio_host = 'https://api.weatherbit.io/v2.0'
    wio_apikey = '1389da161d44471ba20afb597430e41a'

    def __init__(self):
        pass
    
    @jwt_required
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('ip', location = 'args', default=None)
        args = parser.parse_args()

        ## Step - 1 - check lon lat from ip
        rq = requests.get(self.wio_host + '/ip', params = {'ip':args['ip'], 'key':self.wio_apikey})
        geo = rq.json()
        print(geo)
        lat = geo['latitude']
        lon = geo['longitude']

        ## Step - 2 - get current weather from lat lon
        rq = requests.get(self.wio_host + '/current', params = {'lat':lat, 'lon':lon, 'key': self.wio_apikey})
        current = rq.json()

        return {
            'city': geo['city'],
            'organization': geo['organization'],
            'timezone': geo['timezone'],
            'current_weather': {
                'date': current['data'][0]['datetime'],
                'temp': current['data'][0]['temp']
            }
        }

api.add_resource(PublicGetCurrentWeather, '/ip')