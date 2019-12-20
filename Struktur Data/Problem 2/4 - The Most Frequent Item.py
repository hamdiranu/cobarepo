def mostFrequentItem(arr):
    newlst=list(set(arr))
    out=[]
    ganti = True
    while ganti == True:
        ganti = False
        for i in range(len(newlst)-1):
            vardumb=0
            if arr.count(newlst[i+1])<arr.count(newlst[i]):
                vardumb = newlst[i]
                newlst[i] = newlst[i+1]
                newlst[i+1] = vardumb
                ganti = True
    for i in newlst:
        inpiut=i+'({})'.format(arr.count(i))
        out.append(inpiut)
    b=', '.join(out)
    return b
print('')
print(mostFrequentItem(['asus', 'asus', 'samsung', 'iphone', 'iphone', 'asus', 'asus']))
# 'samsung(1), iphone(2), asus(4)'
print('')
print(mostFrequentItem(['9', 'b', 'b', 'c', '9', '9', 'b', '9', '2', '2']))
# 'c(1), 2(2), b(3), 9(4)'
print('')
print(mostFrequentItem(['book', 'laptop', 'iPod']))
# 'book(1), laptop(1), iPod(1)'
print('')       