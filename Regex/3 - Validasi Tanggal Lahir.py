import re
import pprint

def validasiTanggalLahir(arr):
  # you can only write your code here!
  def tahunKabisat(tahun):
    if tahun % 4 == 0 :
      if tahun % 400 == 0 :
        return True
      else:
        if tahun % 100 == 0 :
            return False
        else:
            return True
    else:
      return False

  final={
    'invalid':[],
    'valid':[]
  }
  tanggal31=['01','03','05','07','08','10','12']
  for i in arr :
    pattern = '((19|20)[0-9][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[0-1])'
    tanggal = re.search(pattern,i['tgl_lahir'])
    alert=0
    if tanggal: 
      if tanggal.group(3) in tanggal31:
        batas = 31
      else :
        if tanggal.group(3) == '02':
          if tahunKabisat(int(tanggal.group(1))):
            batas = 29
          else :
            batas = 28
        else:
          batas = 30
      if int(tanggal.group(4))==29 and tahunKabisat(int(tanggal.group(1))) != True:
        i['alasan']=['penunjuk hari dalam bulan terkait tidak valid (cek aturan tahun kabisat)']
        alert += 1
        final['invalid'].append(i)
        continue
      if int(tanggal.group(1))<1900 or int(tanggal.group(1))>2099:
        i['alasan']=['tahun di luar batas yang ditentukan']
        alert += 1
        final['invalid'].append(i)
      else:
        if int(tanggal.group(3))>12 or int(tanggal.group(3))<1 :
          i['alasan']=['bulan di luar batas yang ditentukan']
          alert += 1
          final['invalid'].append(i)
        else :
          if int(tanggal.group(4))>batas:
            if batas == 29 :
              i['alasan']=['penunjuk hari dalam bulan terkait tidak valid (cek aturan tahun kabisat)']
              alert += 1
              final['invalid'].append(i)
            else :
              i['alasan']=['hari di luar batas yang ditentukan']
              alert += 1
              final['invalid'].append(i)
    else :
      if int(i['tgl_lahir'][:4]) > 2099:
        i['alasan']=['tahun di luar batas yang ditentukan']
        alert += 1
        final['invalid'].append(i)
      elif int(i['tgl_lahir'][5:7]) > 12:
        i['alasan']=['bulan di luar batas yang ditentukan']
        alert += 1
        final['invalid'].append(i)
      elif int(i['tgl_lahir'][-2:]) > 31:
        i['alasan']=['hari di luar batas yang ditentukan']
        alert += 1
        final['invalid'].append(i)  
    if alert == 0:
      final['valid'].append(i)

  return final


  

# Driver Code
print('')
pprint.pprint(validasiTanggalLahir([
  {'nama':'Jane Doe', 'tgl_lahir': '1992-10-31'},
  {'nama':'Jack Doe', 'tgl_lahir': '1997-02-29'},
  {'nama':'Donny Doe', 'tgl_lahir': '1988-12-01'}
]))

'''
{
  'invalid': [
    {'tgl_lahir': '1997-02-29', 'nama': 'Jack Doe', 
    'alasan': ['penunjuk hari dalam bulan terkait tidak valid (cek aturan tahun kabisat)']}
  ],
  'valid': [
    {'tgl_lahir': '1992-10-31', 'nama': 'Jane Doe'}, 
    {'tgl_lahir': '1988-12-01', 'nama': 'Donny Doe'}
  ]
}
'''
print("")

pprint.pprint(validasiTanggalLahir([
   {'nama':'Bayu Aji', 'tgl_lahir': '1983-04-31'},
   {'nama':'Tia Nugroho', 'tgl_lahir': '1984-08-29'},
   {'nama':'Ariel Bayu', 'tgl_lahir': '1988-07-32'}
]))

'''
{
  'invalid': [
    {'tgl_lahir': '1988-07-32', 'alasan': ['hari di luar batas yang ditentukan'], 'nama': 'Ariel Bayu'},
    {'tgl_lahir': '1983-04-31', 'nama': 'Bayu Aji', ‘alasan’: [‘hari di luar batas yang ditentukan’]}
  ],
  'valid': [
    {'tgl_lahir': '1984-08-29', 'nama': 'Tia Nugroho'}
  ]
}
'''
print('')
pprint.pprint(validasiTanggalLahir([
  {'nama':'Tulus Saputra', 'tgl_lahir': '2100-05-31'},
  {'nama':'Sumitro Doe', 'tgl_lahir': '2002-13-31'},
  {'nama':'Juni Talira', 'tgl_lahir': '2001-09-12'}
]))

'''
{
  'invalid': [
    {'nama': 'Tulus Saputra', 'alasan': ['tahun di luar batas yang ditentukan'], 'tgl_lahir': '2100-05-31'},
    {'nama': 'Sumitro Doe', 'alasan': ['bulan di luar batas yang ditentukan'], 'tgl_lahir': '2002-13-31'}],
  'valid': [
    {'nama': 'Juni Talira', 'tgl_lahir': '2001-09-12'}
  ]
}
'''
