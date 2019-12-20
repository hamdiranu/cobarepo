# import json
# from . import client, create_token, reset_db

# class TestBookCrud():

#     idPerson = 0
#     reset_db()

#     # ======================================= POST ==================================== #

#     def test_book_post_internal(self, client):
#         token = create_token(True)

#         data = {
#             "title":"titanic",
#             "isbn":"1-234-5678-9101112-13",
#             "writer":"hamdira"
#         }

#         res = client.post('/book', json = data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
#         assert res.status_code == 200
#         assert res_json['id']>0
#         # assert res_json['client_secret'] == hashlib.md5(data['client_secret'])
        
#         self.idPerson = res_json['id']

#     def test_book_post_noninternal(self, client):
#         token = create_token(False)

#         data = {
#             "title":"titanic",
#             "isbn":"1-234-5678-9101112-13",
#             "writer":"hamdira"
#         }

#         res = client.post('/book', json = data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
#         assert res.status_code == 403
#         # assert res_json['client_secret'] == hashlib.md5(data['client_secret'])

#     # ======================================= GET ==================================== #

#     def test_book_get_id_internal(self, client):
#         token = create_token(True)
#         res = client.get('/book/1',
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
        
#         assert res.status_code == 200

#     def test_book_get_id_internal_id_outrange(self, client):
#         token = create_token(True)
#         res = client.get('/book/100',
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
#         assert res.status_code == 404
    
#     # ======================================= GET_All ==================================== #

#     def test_book_get_all_internal_writer_desc(self, client):
#         token = create_token(True)

#         data = {
#             "p":1,
#             "rp":25,
#             "writer":"hamdira",
#             "orderby":"writer",
#             "sort":"desc"
#         }

#         res = client.get('/book',query_string= data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
        
#         assert res.status_code == 200

#     def test_book_get_all_internal_writer_asc(self, client):
#         token = create_token(True)

#         data = {
#             "p":1,
#             "rp":25,
#             "writer":"hamdira",
#             "orderby":"writer",
#             "sort":"asc"
#         }

#         res = client.get('/book',query_string= data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)

#         assert res.status_code == 200

#     # ======================================= PUT ==================================== #

#     def test_book_put_internal(self, client):
#         token = create_token(True)

#         data = {
#             "title":"Alabasta",
#             "isbn":"1-234-5678-9101112-23",
#             "writer":"hamdira"
#         }

#         res = client.put('/book/1', json = data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
#         assert res.status_code == 200
#         assert res_json['id']>0
#         # assert res_json['client_secret'] == hashlib.md5(data['client_secret'])
        
#         self.idPerson = res_json['id']

#     def test_book_put_internal_id_notfound(self, client):
#         token = create_token(True)

#         data = {
#             "title":"titanic",
#             "isbn":"1-234-5678-9101112-13",
#             "writer":"hamdira"
#         }

#         res = client.put('/book/100', json = data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
#         assert res.status_code == 404
        
#     def test_book_put_noninternal(self, client):
#         token = create_token(False)

#         data = {
#             "title":"titanic",
#             "isbn":"1-234-5678-9101112-13",
#             "writer":"hamdira"
#         }

#         res = client.put('/book/1', json = data,
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
#         assert res.status_code == 403
#         # assert res_json['client_secret'] == hashlib.md5(data['client_secret'])
        
#     # ======================================= DELETE ==================================== #

#     def test_book_delete_id_internal(self, client):
#         token = create_token(True)
#         res = client.delete('/book/1',
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
        
#         assert res.status_code == 200

#     def test_book_delete_id_internal_idnotfound(self, client):
#         token = create_token(True)
#         res = client.delete('/book/100',
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
        
#         assert res.status_code == 404

#     # ======================================= PATCH ==================================== #

#     def test_book_patch_internal(self, client):
#         token = create_token(True)
#         res = client.patch('/book',
#         headers={'Authorization': 'Bearer ' + token})

#         res_json = json.loads(res.data)
        
#         assert res.status_code == 501