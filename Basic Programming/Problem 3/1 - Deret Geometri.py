def tentukanDeretGeometri(arr):
    for i in range(0,len(arr)-2):
        if arr[i+1] / arr[i] == arr[i+2] / arr[i+1] :
            print(' ') # sebagai jarak dengan line sebelumnya
            return True
            
        else :
            print(' ') # sebagai jarak dengan line sebelumnya
            return False
            
    

print(tentukanDeretGeometri([1, 3, 9, 27, 81]))
print(tentukanDeretGeometri([2, 4, 8, 16, 32]))
print(tentukanDeretGeometri([2, 4, 6, 8]))
print(tentukanDeretGeometri([2, 6, 18, 54]))
print(tentukanDeretGeometri([1, 2, 3, 4, 7, 9]))
