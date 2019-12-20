import json
from . import client, create_token, reset_db
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints.Rent.model import Rents


class TestRentCrud():

    idPerson = 0
    reset_db()

    # ======================================= POST ==================================== #

    def test_rent_post_noninternal(self, client):
        token = create_token(False)

        data = {
            "book_id":1,
            "user_id":1
        }

        res = client.post('/rent', json = data,
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        assert res.status_code == 200
        # assert res_json['client_secret'] == hashlib.md5(data['client_secret'])

    # ======================================= GET ==================================== #

    def test_rent_get_id_internal(self, client):
        token = create_token(True)
        res = client.get('/rent/1',
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        
        assert res.status_code == 403

    def test_rent_get_id_noninternal(self, client):
        token = create_token(False)
        res = client.get('/rent/1',
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_rent_get_id_noninternal_id_outrange(self, client):
        token = create_token(False)
        res = client.get('/rent/100',
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        assert res.status_code == 404
    
    # ======================================= GET_All ==================================== #

    def test_rent_get_all_noninternal(self, client):
        token = create_token(False)

        data = {
            "p":1,
            "rp":25,
            "book_id":1,
            "user_id":1
        }

        res = client.get('/rent',query_string= data,
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_rent_get_all_internal(self, client):
        token = create_token(True)

        data = {
            "p":1,
            "rp":25,
            "book_id":1,
            "user_id":1
        }

        res = client.get('/rent',query_string= data,
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)

        assert res.status_code == 403

    # ======================================= DELETE ==================================== #

    def test_rent_delete_id_internal(self, client):
        token = create_token(True)
        res = client.delete('/rent/1',
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        
        assert res.status_code == 200

    def test_rent_delete_id_internal_idnotfound(self, client):
        token = create_token(True)
        res = client.delete('/rent/100',
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
        
        assert res.status_code == 404

    # ======================================= PATCH ==================================== #

    def test_rent_patch_internal(self, client):
        token = create_token(True)
        res = client.patch('/rent',
        headers={'Authorization': 'Bearer ' + token})

        res_json = json.loads(res.data)
       
        assert res.status_code == 501