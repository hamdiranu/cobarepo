def urutanList(lst):
    ganti = True
    while ganti == True:
        ganti = False
        for i in range(len(lst)-1):
            vardumb=0
            if lst[i]>lst[i+1]:
                vardumb = lst[i]
                lst[i] = lst[i+1]
                lst[i+1] = vardumb
                ganti = True
    return lst

def howManyGifts(maxBudget, gifts) :
    gift = []
    lst=urutanList(gifts)
    for i in range(len(lst)):
        if maxBudget >= lst[i]:
            gift.append(lst[i])
            maxBudget=maxBudget-lst[i]
    banyakgift=len(gift)
    return banyakgift

print(howManyGifts(30000, [15000, 12000, 5000, 3000, 10000])) # 4
print(howManyGifts(10000, [2000, 2000, 3000, 1000, 2000, 10000])) # 5
print(howManyGifts(4000, [7500, 1500, 2000, 3000])) # 2
print(howManyGifts(50000, [25000, 25000, 10000, 15000])) # 3
print(howManyGifts(0, [10000, 3000])) # 0

