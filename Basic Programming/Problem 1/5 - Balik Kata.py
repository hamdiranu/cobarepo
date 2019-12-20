
# Input 1
# Memasukkan input
Nama = "John Doe"

# Proses
hasil = []
posis = len(Nama) - 1

for i in range(posis, 0, -1):
    hasil.append(str(Nama[i]))
    
hasil.append(Nama[0]) # nama masih dalam list dengan perantara ,

# Hasil (Output)
print(''.join(hasil)) # untuk mencetak nama


# Input 2
# Memasukkan input
Nama = "Hello World and Coders"

# Proses
hasil=[]
posis=len(Nama)-1

for i in range(posis,0,-1):
    hasil.append(str(Nama[i]))
    
hasil.append(Nama[0]) # nama masih dalam list dengan perantara ,

# Hasil (Output)
print(''.join(hasil)) # untuk mencetak nama