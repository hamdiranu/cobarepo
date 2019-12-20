def palindrome(kata):
    # Proses
    hasil = []
    posis = len(kata) - 1

    for i in range(posis, 0, -1) :
        hasil.append(str(kata[i]))
        
    hasil.append(kata[0]) # kata masih dalam list dengan perantara ,
    akhir=''.join(hasil) # untuk menyambung jadi 1 string
    if akhir == kata :
        return True
    else :
        return False

print(palindrome('katak'))
print(palindrome('blanket'))
print(palindrome('civic'))
print(palindrome('kasur rusak'))
print(palindrome('mister'))