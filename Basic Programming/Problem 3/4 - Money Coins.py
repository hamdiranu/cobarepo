def convertToCoin(value):
    output = []
    pecahan=[10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 1]
    for i in range(len(pecahan)):
        while value >= pecahan[i]:
            output.append(pecahan[i])
            value=value-pecahan[i]
 
    return output     

print(convertToCoin(543))
print(convertToCoin(7752))
print(convertToCoin(37454))
        
        


