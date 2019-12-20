def palindromeRecursive(sentence) :
    if len(sentence)==1:
        return True
    else :
        if sentence[0]==sentence[-1]:
            return palindromeRecursive(sentence[1:-1])
        else :
            return False

print(palindromeRecursive('katak')) # true
print(palindromeRecursive('blanket')) # false
print(palindromeRecursive('civic')) # true
print(palindromeRecursive('kasur rusak')) # true
print(palindromeRecursive('mister')) # false