def angkaSatuDua(numbers):
    for i in numbers:
        if i == 1 :
            if numbers[numbers.index(i)+1]!=2:
                for j in numbers:
                    if j==2 : 
                        numbers[numbers.index(j)] = numbers[numbers.index(i)+1] 
                        numbers[numbers.index(i)+1] = 2
            
    return numbers

print(angkaSatuDua([2, 1, 3, 1, 6, 2])) # [3, 1, 2, 1, 2, 6]
print(angkaSatuDua([4, 1, 4, 2])) # [4, 1, 2, 4]
print(angkaSatuDua([7, 1, 8, 2, 2, 1, 3])) # [7, 1, 2, 8, 3, 1, 2]
print(angkaSatuDua([1, 7, 8, 2, 2, 1, 5])) # [1, 2, 8, 7, 5, 1, 2]
print(angkaSatuDua([1, 5, 3, 4, 2, 6, 7])) # [1, 2, 3, 4, 5, 6, 7]


                        


