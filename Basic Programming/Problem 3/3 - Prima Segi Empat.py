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

def prismaSegiempat(P, L, X):
    list_prisma=[]
    for i in range(1,50):
        if angkaprima(i) == True:
            list_prisma.append(" "+str(i))
    
    gabung = []
    banyaknya_prim = P*L
    satu=[' 1']
    if X == 1 :
        list_prisma = satu + list_prisma
    else :
        list_prisma=list_prisma[list_prisma.index(" "+str(X)):]
    total = 0
    for i in range(1,(P*L)+1):
        total=total+int(list_prisma[i])

    new=[]
    for i in range(0,len(list_prisma)-P,P):
        listbaru = []
        listbaru.append(list_prisma[i+1:i+P+1])
        
        string=''.join(listbaru[0])
        gabung.append(string)
    i = 1
    while i <= L:
        print(gabung[i-1])
        i += 1
    return("Total: {}".format(total))

print(prismaSegiempat(2, 3, 13))
print('')
print(prismaSegiempat(5, 2, 1))
print('')
    



