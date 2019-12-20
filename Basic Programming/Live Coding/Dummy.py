lst=[1,2,3,4]
b=lst[0:2]
print(b)

def angkaSatuDua(numbers):
    for i in numbers:
        if i == 1 :
            print(numbers[numbers.index(i):])
            if numbers[numbers.index(i)+1]!=2:
                for j in numbers:
                    if j==2 : 
                        numbers[numbers.index(j)] = numbers[numbers.index(i)+1] 
                        numbers[numbers.index(i)+1] = 2

    return numbers


print(angkaSatuDua([2, 1, 3, 1, 6, 2])) # [3, 1, 2, 1, 2, 6]