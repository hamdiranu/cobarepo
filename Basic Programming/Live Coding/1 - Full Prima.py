def angkaprima(angka):
    hasil=[]
    faktor = 0 # initial value untuk jumlah faktor
    for i in range(1, angka+1):
        if angka % i == 0 :
            faktor += 1
            hasil.append(i)
    if len(hasil)==2:
        return True
    else:
        return False

def fullPrima(bilangan):
    hasil=[]
    faktor = 0 # initial value untuk jumlah faktor
    for i in range(1, bilangan+1):
        if bilangan % i == 0 :
            faktor += 1
            hasil.append(i)
    if len(hasil)==2:
        checkperbilangan=[]
        bilangan=str(bilangan)
        for i in range(len(bilangan)):
            checkperbilangan.append(int(bilangan[i]))
        d=0
        for i in checkperbilangan:
            if angkaprima(i) == True :
                d+=1
        if d==len(checkperbilangan):
            return ("Ya")
        else :
            return ("Tidak")
    else:
        return ("Tidak")
    

print(fullPrima(2)) #Ya
print(fullPrima(3)) # Ya
print(fullPrima(11)) # Tidak
print(fullPrima(13)) # Tidak
print(fullPrima(23)) # Ya
print(fullPrima(29)) # Tidak
print(fullPrima(37)) # Ya
print(fullPrima(41)) # Tidak
print(fullPrima(43)) # Tidak
print(fullPrima(53)) # Ya

