def checkPalindrom(value):
    num=value
    lst=[]
    while num%10 != num:
        angka=num%10
        if angka == 0:
            lst.append(0)
        else:
            lst.append(angka)
        num=int((num-angka)/10)
    lst.append(int(num))
    out=0
    for i in range(1,len(lst)+1):
        tambahan=lst[-i]*(10**(i-1))
        out+=tambahan

    if out == value :
        return True
    else :
        return False


def angkaPalindrome(value) :
    yes=0
    for i in range(value+1,value+50):
        if checkPalindrom(i) == True:
            return i
            yes+=1
            break
    

print(angkaPalindrome(8))
print(angkaPalindrome(10))
print(angkaPalindrome(117))
print(angkaPalindrome(175))
print(angkaPalindrome(1000))
