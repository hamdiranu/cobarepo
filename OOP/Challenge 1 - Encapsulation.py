class Cat:
    def __init__(self, fur_color, num_of_leg):
        self.fur_color = fur_color
        self._num_of_leg = num_of_leg

    def show_identity(self):
        print("Saya kucing dengan detail, Warna Bulu: {} dengan jumlah kaki : {}".format(self.fur_color,self._num_of_leg))

cat1=Cat('Hitam', 4)
cat2=Cat('Putih', 3)
cat3=Cat('Hitam Putih', 4)
cat4=Cat('Poleng poleng', 3)
cat5=Cat('bintik bintik', 4)

cat1.show_identity()
cat2.show_identity()
cat3.show_identity()
cat4.show_identity()
cat5.show_identity()

print('')

class Fish:
    def __init__(self, type, feed):
        self._type = type
        self.feed = feed

    def show_identity(self):
        print("saya ikan dengan detail, Jenis: {}, makanan: {}".format(self._type, self.feed))

fish1 = Fish('paus', 'plankton')
fish2 = Fish('cupang', 'cacing')
fish3 = Fish('arwana', 'jangkrik')
fish4 = Fish('sapu-sapu', 'pelet')

fish1.show_identity()
fish2.show_identity()
fish3.show_identity()
fish4.show_identity()

print('')

class Flower:
    def __init__(self, nama, color, num_of_petal):
        self.nama = nama
        self._color = color
        self.__num_of_petal = num_of_petal

    def show_identity(self):
        print("saya Bunga dengan detail, Jenis: {}, color: {}, num of petal: {}".format(self.nama, self._color, self.__num_of_petal))

flower1 = Flower('bangkai', 'merah', 12)
flower2 = Flower('anggrek', 'putih', 8 )
flower3 = Flower('mawar', 'merah', 3)
flower4 = Flower('melati', 'kuning', 5)

flower1.show_identity()
flower2.show_identity()
flower3.show_identity()
flower4.show_identity()

print('')

class Car:
    def __init__(self, type, color, num_of_tire):
        self.type = type
        self.color = color
        self.__num_of_tire = num_of_tire

    def show_identity(self):
        print("saya mobil dengan detail, Type: {}, color: {}, num of tire: {}".format(self.type, self.color, self.__num_of_tire))

car1 = Car('sedan', 'merah', 4)
car2 = Car('truk', 'hijau', 6)
car3 = Car('tronton', 'coklat', 12)
car4 = Car('angkot', 'kuning', 4)

car1.show_identity()
car2.show_identity()
car3.show_identity()
car4.show_identity()

print('')