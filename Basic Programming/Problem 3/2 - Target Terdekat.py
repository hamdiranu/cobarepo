def targetTerdekat(arr):
    terkecil=[]
    for i in range(len(arr)):
        if arr[i] == 'x' :
            for j in range(len(arr)):
                if arr[j]== 'o':
                    jarak=abs(j-i)
                    terkecil.append(jarak)
    min=1000000
    for i in terkecil :
        if i < min :
            min = i
    if min == 1000000 :
        min = 0
    return(min)


print(targetTerdekat([' ', ' ', 'o', ' ', ' ', 'x', ' ', 'x']))
print(targetTerdekat(['o', ' ', ' ', ' ', 'x', 'x', 'x']))
print(targetTerdekat(['x', ' ', ' ', ' ', 'x', 'x', 'o', ' ']))
print(targetTerdekat([' ', ' ', 'o', ' ']))
print(targetTerdekat([' ', 'o', ' ', 'x', 'x', ' ', ' ', 'x']))