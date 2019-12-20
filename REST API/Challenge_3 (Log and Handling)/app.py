# app.py

from flask import Flask, request
from flask_restful import Resource, Api
import json, logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
api = Api(app, catch_all_404s = True)

from blueprints.User.resource import bp_user

######################
#  Import Blueprint  #
######################

app.register_blueprint(bp_user, url_prefix = '/user')

@app.after_request
def after_request(response):
    try :
        requestData = request.get_json()
    except Exception as e :
        requestData = request.args.to_dict()
    if response.status_code == 200 :
        app.logger.info("REQUEST_LOG\t%s",json.dumps({
            'status_code':response.status_code,
            'method':request.method,
            'code':response.status,
            'uri':request.full_path,
            'request': request.args.to_dict(),
            'response': json.loads(response.data.decode('utf-8'))
            })
        )

    elif response.status_code == 501 :
        app.logger.error("REQUEST_LOG\t%s",json.dumps({
            'status_code':response.status_code,
            'method':request.method,
            'code':response.status,
            'uri':request.full_path,
            'request': request.args.to_dict(),
            'response': json.loads(response.data.decode('utf-8'))
            })
        )

    else:
        app.logger.warning("REQUEST_LOG\t%s",json.dumps({
            'status_code':response.status_code,
            'method':request.method,
            'code':response.status,
            'uri':request.full_path,
            'request': request.args.to_dict(),
            'response': json.loads(response.data.decode('utf-8'))
            })
        )
    return response


if __name__ == '__main__':

    ## define log format and create a rotating log with max size of 10MB and max backup up to 10 files
    logging.getLogger().setLevel('INFO')
    formatter = logging.Formatter("[%(asctime)s]{%(pathname)s:%(lineno)d} %(levelname)s-%(message)s")
    log_handler = RotatingFileHandler("%s/%s" %(app.root_path,'storage/log/app.log'),maxBytes=10000, backupCount=10)
    log_handler.setLevel(logging.INFO)
    log_handler.setFormatter(formatter)
    app.logger.addHandler(log_handler)

    app.run(debug = True, host = '0.0.0.0', port = 4000)

