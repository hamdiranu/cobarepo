def string_acak(stringSatu, stringDua):
    alert=0
    if len(stringSatu)!=len(stringDua):
        return False
    else :
        for i in stringSatu:
            if stringSatu.count(i)==stringDua.count(i):
                continue
            else:
                alert+=1
        if alert !=0 :
            return False
        else:
            return True
    
    
print(" ")
print(string_acak('malang', 'agmlan')) # True
print(string_acak('alterra', 'rerlata')) # True
print(string_acak('alterra', 'terlata')) # False
print(string_acak('python', 'nothyd')) # False
print(string_acak('python', 'nothyp')) # True
print(" ")
