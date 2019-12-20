def pasanganTerbesar(num):
    num = str(num)
    pasangannum = []
    for i in range(0,len(num) - 1 ) :
        pasangannum.append(num[i : i+2])
    max = 0 # sebagai variabel sementara
    for i in pasangannum :
        i = int(i)
        if i > max :
            max = i
    return (max)

print(pasanganTerbesar(641573))
print(pasanganTerbesar(12783456))
print(pasanganTerbesar(910233))
print(pasanganTerbesar(71856421))
print(pasanganTerbesar(79918293))
