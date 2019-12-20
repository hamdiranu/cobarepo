def mengelompokkanAngka(arr) :
    List_output = [[],[],[]]
    for i in range(len(arr)) :
        if arr[i] % 2 == 0 :
            if arr[i] % 3 == 0 :
                List_output[2].append(arr[i])
            else :
                List_output[0].append(arr[i])
        else :
            if arr[i] % 3 == 0 :
                List_output[2].append(arr[i])
            else :
                List_output[1].append(arr[i])
    return (List_output)

print(mengelompokkanAngka([2, 4, 6]))
# [ [2, 4], [], [6] ]
print(mengelompokkanAngka([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [ [ 2, 4, 8 ], [ 1, 5, 7 ], [ 3, 6, 9 ] ]
print(mengelompokkanAngka([100, 151, 122, 99, 111]))
# [ [ 100, 122 ], [ 151 ], [ 99, 111 ] ]
print(mengelompokkanAngka([]))
# [ [], [], [] ]


