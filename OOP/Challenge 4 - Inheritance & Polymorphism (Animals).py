class Animals:
    name = ''
    Jenis_makanan = ''
    Gigi_binatang = ''
    def __init__(self, name, Jenis_makanan, Gigi_binatang):
        self.name = name
        self.Jenis_makanan = Jenis_makanan
        self.Gigi_binatang = Gigi_binatang
    
    def identify_myself(self):
        print( "Hi I'm Parent of All Vehicles, My Name is {}".format(self.name))

class Herbivor(Animals):
    def __init__(self, name, Jenis_makanan, Gigi_binatang):
        super().__init__(name, Jenis_makanan, Gigi_binatang)

    def identify_myself(self):
        print( "Hi I'm Herbivor, My Name is {}, My Food is '{}', I Have {} teeth".format(self.name, self.Jenis_makanan, self.Gigi_binatang))

class Carnivor(Animals):
    def __init__(self, name, Jenis_makanan, Gigi_binatang):
        super().__init__(name, Jenis_makanan, Gigi_binatang)

    def identify_myself(self):
        print( "Hi I'm Carnivor, My Name is {}, My Food is '{}', I Have {} teeth".format(self.name, self.Jenis_makanan, self.Gigi_binatang))


class Omnivor(Animals):
    def __init__(self, name, Jenis_makanan, Gigi_binatang):
        super().__init__(name, Jenis_makanan, Gigi_binatang)

    def identify_myself(self):
        print( "Hi I'm Omnivor, My Name is {}, My Food is '{}', I Have {} teeth".format(self.name, self.Jenis_makanan, self.Gigi_binatang))

print('')
binatang = Animals('Binatang','rumput', 'tajam')
binatang.identify_myself()

print('')
kambing = Herbivor('Kambing','tumbuhan','tumpul')
kambing.identify_myself()

print('')
singa = Carnivor('Singa','daging','tajam')
singa.identify_myself()

print('')
ayam = Omnivor('Ayam','semua','tajam dan tumpul')
ayam.identify_myself()
print('')