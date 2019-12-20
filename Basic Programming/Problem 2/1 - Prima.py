def angkaprima(angka):
    print("Input: " + str(angka))
    hasil=[]
    faktor = 0 # initial value untuk jumlah faktor
    for i in range(1, angka+1):
        if angka % i == 0 :
            faktor += 1
            hasil.append(i)
    print(hasil)
    if len(hasil)==2:
        return True
    else:
        return False

print(angkaprima(1))
print(angkaprima(3))
print(angkaprima(7))
print(angkaprima(6))
print(angkaprima(23))
