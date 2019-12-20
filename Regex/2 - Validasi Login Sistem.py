import re

def validasiLogin(email, password):
  database = [
    {'email':'johndoe@gmail.com', 'password': '123456'},
    {'email':'johndoe@yahoo.co.id', 'password': '123456'},
    {'email':'john_doe@gmail.com', 'password': 'asdfasdfds'}
  ]

  hasil = {}

  patternemail = '([a-zA-Z_]+@[a-z]+\.[a-zA-Z.]{2,3})'
  patternpass = '([a-zA-z0-9]{6,10})'
  a= database[0]
  b= database[1]
  c= database[2]

  if re.search(patternemail,email):
    if re.search(patternpass,password):         
        if email == a['email'] or email == b['email'] or email == c['email']:
          if password == a['password'] or password == b['password'] or password == c['password']:
            hasil['pesan'] = []
            hasil['status'] = True
            return hasil
          else:
            hasil['pesan'] = ['password tidak valid']
            hasil['status'] = False
            return hasil
        else:
          hasil['pesan'] = ['email tidak terdaftar dalam database']
          hasil['status'] = False
          return hasil
    else :
      hasil['pesan'] = ['password tidak valid']
      hasil['status'] = False
      return hasil
  else :
    hasil['pesan'] = ['email tidak valid']
    hasil['status'] = False
    return hasil

# Driver Code
print(validasiLogin('johndoe@gmail.com','123456'))
# {'pesan': [], 'status': True}
print(validasiLogin('jane@gmail.com','1245'))
# {'pesan': ['password tidak valid'], 'status': False
print(validasiLogin('johndoe_gmail.com','123456'))
# {'pesan': ['email tidak valid'], 'status': False}
print(validasiLogin('johndoe@yahoo.co.id','12abcd'))
# {'pesan': [password tidak valid], 'status': False}
print(validasiLogin('john_doe@gmail.com','asdfasdfds'))
# {'pesan': [], 'status': True}