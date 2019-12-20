def cariModus(arr) :
    jmlh = 1
    modus = -1
    if arr.count(arr[0]) == len(arr) :
        return -1
    else :
        for i in arr :
            if arr.count(i) > jmlh:
                modus = i
        return modus

print(cariModus((10, 4, 5, 2, 4))) # 4
print(cariModus((5, 10, 10, 6, 5))) # 5
print(cariModus((10, 3, 1, 2, 5))) # -1
print(cariModus((1, 2, 3, 3, 4, 5))) # 3
print(cariModus((7, 7, 7, 7, 7))) # -1