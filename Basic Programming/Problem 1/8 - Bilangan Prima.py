# Input 1
n = 3
print("Input: " + str(n))
hasil=[]
faktor = 0 # initial value untuk jumlah faktor
for i in range(1, n+1):
    if n % i == 0 :
        faktor += 1
        hasil.append(i)
if len(hasil)==2:
    print("Output: Bilangan Prima")
else:
    print("Output: Bukan Bilangan Prima")

print(" ")

# Input 2
n = 7
print("Input: " + str(n))
hasil=[]
faktor = 0 # initial value untuk jumlah faktor
for i in range(1, n+1):
    if n % i == 0 :
        faktor += 1
        hasil.append(i)
if len(hasil)==2:
    print("Output: Bilangan Prima")
else:
    print("Output: Bukan Bilangan Prima")

print(" ")

# Input 3
n = 10
print("Input: " + str(n))
hasil=[]
faktor = 0 # initial value untuk jumlah faktor
for i in range(1, n+1):
    if n % i == 0 :
        faktor += 1
        hasil.append(i)
if len(hasil)==2:
    print("Output: Bilangan Prima")
else:
    print("Output: Bukan Bilangan Prima")