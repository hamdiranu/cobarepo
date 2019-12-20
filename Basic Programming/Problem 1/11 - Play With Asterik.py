# # Pattern satu
# print(" ") # diprint sebagai jarak dengan perintah sebelumnya
# Pattern = '* '
# n = 5
# i = 1
# while i < n+1:
#     print(Pattern*i)
#     i += 1

# Pattern dua
# print(' ')
# Pattern = ' *'
# n = 5
# i = 1
# while i < n+1:
#     print(' '*(n-i)+Pattern*i)
#     i += 1
# print(' ')

# Pattern tiga
# print(' ')
# n = 5 
# i = 1
# b=[]
# while i < n+2:
#     for j in range(1,i):
#         b.append(str(j))
#     c=''.join(b)
#     print(c)
#     i += 1
#     b=[]
# print(' ')

# Pattern empat
print('')
n = 5
i = 1
d=2
e=1
f=2
b=[]
while i < n+7:
    for j in range(i,d):
        b.append(str(j)+' ')
    c=''.join(b)
    print(c)
    i += e
    d += f
    b=[]
    e+=1 # sebagai penambahan range bagian kiri
    f+=1 # sebagai penambahan range bagian kiri
print('')

# # Pattern lima 
# print(' ')
# Pattern = ' *'
# n = 5
# i = 1
# while i < n+1:
#     print('  '*((n)-i)+Pattern*i)
#     i += 1
# print(' ')