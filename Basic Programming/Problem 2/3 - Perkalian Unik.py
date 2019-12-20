def perkalianUnik(arr):
    total = 1
    hasil = []
    List = []
    for i in arr :
        for j in arr :
            if i != j:
                hasil = hasil*j
                List.append(hasil)
            else :
                continue
               return (hasil)

print(perkalianUnik([2, 4, 6]))