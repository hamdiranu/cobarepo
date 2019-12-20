def mini(lst):
    mini = float('inf')
    for i in lst:
        if i <= mini:
            mini = i
    return mini

def jumbo(lst):
    jumbo=float('-inf')
    for i in lst:
        if i >= jumbo:
            jumbo = i
    return jumbo
    
def statistik(kata, arr1, arr2):
    if kata == 'min' :
        return mini(arr1),mini(arr2)
    elif kata == 'max' :
        return (jumbo(arr1),jumbo(arr2))

print(statistik('min', [1, 1, 1] , [8, 15, 17, 9])) # 1 8
print(statistik('max', [4, 8, 9, 12] , [33, 88, 99 ,11])) # 12 99
print(statistik('min', [1, 2, 5, 2, 2] , [67, 45, 55])) # 1 45
print(statistik('max', [6, 2, 4, 10, 8, 2] , [6, 5, 13, 23])) # 10 23
print(statistik('min', [5, 11, 18, 6], [3, 1, 8, 13])) # 5 1






