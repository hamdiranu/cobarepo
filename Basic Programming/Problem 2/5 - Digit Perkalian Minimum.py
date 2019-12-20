def digitPerkalianMinimum(angka):
    masuk=[]
    for i in range(1,angka):
        if angka%i==0 :
            pmbagi1=(len(str(i)))
            b=angka/i
            pmbagi2=(len(str(int(b))))
            masuk.append(pmbagi1+pmbagi2)
    hasil=float('inf')
    for i in masuk :
        if i <= hasil :
            hasil = i
    if hasil == float('inf') :
        return(2)
    else :
        return(hasil)

print(digitPerkalianMinimum(24))
print(digitPerkalianMinimum(90))
print(digitPerkalianMinimum(20))
print(digitPerkalianMinimum(179))
print(digitPerkalianMinimum(1))