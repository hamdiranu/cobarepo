def kaliTerusRekursif(angka):
    hasil = 1
    for i in str(angka):
        hasil = hasil * int(i)
    if len(str(angka)) > 1 :
        return kaliTerusRekursif(hasil)
    else :
        return hasil

print(kaliTerusRekursif(66)) # 8
print(kaliTerusRekursif(3)) # 3
print(kaliTerusRekursif(24)) # 8
print(kaliTerusRekursif(654)) # 0
print(kaliTerusRekursif(1231)) # 6
