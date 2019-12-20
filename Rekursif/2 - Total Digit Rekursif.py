def totalDigitRekursif(angka) :
    if angka == 0 :
        return 0
    else :
        return (angka%10)+totalDigitRekursif(angka//10)
        
print(totalDigitRekursif(512)) # 8
print(totalDigitRekursif(1542)) # 12
print(totalDigitRekursif(5)) # 5
print(totalDigitRekursif(21)) # 3
print(totalDigitRekursif(11111)) # 5
