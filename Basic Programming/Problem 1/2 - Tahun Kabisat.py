# Input nilai tahun
tahun=int(input('Masukkan Tahun: '))

# Proses
if tahun % 4 == 0 :
    if tahun % 400 == 0 :
        print("Tahun kabisat")
    else:
        if tahun % 100 == 0 :
            print("Bukan tahun kabisat")
        else:
            print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")
