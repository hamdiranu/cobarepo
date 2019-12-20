def groupAnimals(animals):
    out=[]
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in alpha:
        perhuruf=[]
        for j in animals:
            if j[0] == i :
                perhuruf.append(j)
        if perhuruf == []:
            continue
        else :
            out.append(perhuruf)
    return out

# Driver Code
print(' ')
print(groupAnimals(['cacing', 'ayam', 'kuda', 'anoa', 'kancil']))
# [ ['ayam', 'anoa'], ['cacing'], ['kuda', 'kancil'] ]
print(' ')
print(groupAnimals(['cacing', 'ayam', 'kuda', 'anoa', 'kancil', 'unta', 'cicak' ]))
# [ ['ayam', 'anoa'], ['cacing', 'cicak'], ['kuda'], ['unta'] ]
print(' ')



