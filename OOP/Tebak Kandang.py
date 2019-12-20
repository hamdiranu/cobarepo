import os, sys, random

if sys.platform.lower() == "win32":
    os.system('color')

# Group of Different functions for different styles
class style():
    RED = lambda x: '\033[31m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    WHITE = lambda x: '\033[37m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

# print(style.YELLOW("Hello, ") + style.RESET("World!"))

class Kandang():
    def __init__(self, angka, huruf, status):
        self.angka = angka
        self.huruf = huruf
        self.status = status

    def tampilan_huruf_angka(self):
        if self.status == 'Buka':
            print('\n| | |\n| {} '.format(self.huruf)+style.RESET('|\n| | |\n')) # dibutuhkan 'reset' agar str stelah self.huruf tidak bewarna
        else :
            print('\n| | |\n| {} |\n| | |\n'.format(self.angka))

    def ganti_status_buka(self):
        self.status = 'Buka'

    def huruf_pada_kandang(self):
        return self.huruf

class Kambing(Kandang):
    def __init__(self, angka):
        super().__init__(angka, style.BLUE('K'), 'Tutup')

class Zebra(Kandang):
    def __init__(self, angka):
        super().__init__(angka, style.RED('Z'), 'Tutup')

class Bebek(Kandang):
    def __init__(self, angka):
        super().__init__(angka, style.YELLOW('B'), 'Tutup')

# Sistem Game
class Board:
    hasil = 0 # berguna agar untuk mengetahui kapan permainan harus berhenti nantinya
    def __init__(self, hasil):
        self.hasil = hasil

    # =========================== Opening ===========================
    def run(self):
        os.system('clear')
        self.hasil=0
        print('\n=====================================\n'+'||'+' '*10+style.BLUE('Tebak Kandang')+' '*10+style.RESET('||\n=====================================\n'))
        print('1: Jumlah Kandang \n99: Exit\n')
        input1=int(input('Pilih Menu: '))
        if input1==1:
            self.kandang()
        elif input1==99:
            print('\n           Terima Kasih telah menggunakan program kami :)\n')
        else:
            print('\nMohon masukkan pilihan yang sesuai')
            self.run()

    # ====================== Masukkan Jumlah Kandang ==========================
    def kandang(self):
        input2=int(input('Masukkan jumlah kandang: '))
        jmlh_kandang=input2
        self.buat_kandang(jmlh_kandang)

    # =========================  Buat Kandang  ==============================
    def buat_kandang(self,jmlh_kandang):
        isi_kandang = []
        for i in range(0,jmlh_kandang):
            index_list_huruf=random.choice(['K','Z','B'])
            if index_list_huruf == 'K':
                isi_kandang.append(Kambing(str(i+1)))
            elif index_list_huruf == 'Z':
                isi_kandang.append(Zebra(str(i+1)))
            elif index_list_huruf == 'B':
                isi_kandang.append(Bebek(str(i+1)))
        self.tampilan_kandang(jmlh_kandang, isi_kandang)
    
    # =========================  Tampilan Kandang  ============================= 
    def tampilan_kandang(self, jmlh_kandang, isi_kandang):
        for i in (isi_kandang):
            i.tampilan_huruf_angka()
        self.pilihan_kandang(jmlh_kandang, isi_kandang)

    # ======================  Pilihan kotak tebakan  ===========================
    def pilihan_kandang(self,jmlh_kandang,isi_kandang):
        pilihan_kotak = 0
        cek_input=[]
        input3 = input('Pilih kandang yang ingin dibuka: ')
        for i in range(1,jmlh_kandang+1):
            cek_input.append(str(i))
        if input3 in cek_input:
            pilihan_kotak = int(input3)
            self.tebakan_user(jmlh_kandang, isi_kandang, pilihan_kotak) 
        else:
            print('\nMohon masukkan input yang sesuai\n')
            self.pilihan_kandang(jmlh_kandang,isi_kandang)

    # ==========================  Tebakan User  ================================
    def tebakan_user(self,jmlh_kandang, isi_kandang, pilihan_kotak):
        tebakan = ''
        print('---------Pilihan---------\n'+style.BLUE('K')+style.RESET(': Kambing'))
        print(style.RED('Z')+style.RESET(': Zebra'))
        print(style.YELLOW('B')+style.RESET(': Bebek\n'))
        input4 = str(input('Masukkan tebakan: '))
        if input4 in ['K','Z','B','k','z','b']:
            tebakan = input4
            self.proses_cek(jmlh_kandang, isi_kandang, pilihan_kotak, tebakan)
        else:
            print('\nMohon masukkan input yang sesuai\n')
            self.tebakan_user(jmlh_kandang, isi_kandang, pilihan_kotak)

    # ============================  Proses  ==================================
    def proses_cek(self,jmlh_kandang, isi_kandang, pilihan_kotak, tebakan):
        os.system('clear')
        print('PERCOBAAN BUKA:\n')
        if style.BLUE(tebakan.upper()) == isi_kandang[pilihan_kotak-1].huruf_pada_kandang() or style.YELLOW(tebakan.upper()) == isi_kandang[pilihan_kotak-1].huruf_pada_kandang() or style.RED(tebakan.upper()) == isi_kandang[pilihan_kotak-1].huruf_pada_kandang():
            isi_kandang[pilihan_kotak-1].ganti_status_buka()
            self.hasil = self.hasil + 1
            for i in (isi_kandang):
                i.tampilan_huruf_angka()
            print(style.GREEN("Tebakan Benar!")+style.RESET(''))

        else :
            for i in (isi_kandang):
                i.tampilan_huruf_angka()
            print(style.YELLOW("Tebakan Salah!")+style.RESET(''))
        
        self.cek_hasil(jmlh_kandang, isi_kandang, pilihan_kotak, tebakan)
    
    # ================ Pengecekan apakah semua kandang telah dibuka ==============
    def cek_hasil(self,jmlh_kandang, isi_kandang, pilihan_kotak, tebakan):
        if self.hasil==len(isi_kandang):
            for i in (isi_kandang):
                i.tampilan_huruf_angka()
            print('Selamat! anda menebak semua kandang\n')
            self.Bye()
        else:
            self.tampilan_kandang(jmlh_kandang, isi_kandang)

    # =================================  OUT  ====================================
    def Bye(self):
        input5=input('Apakah anda ingin mengulangi permainan? (Y/N) :')
        if input5 == "Y" or input5 == "y":
            self.run()
        elif input5 == "N" or input5 == "n":
            print('\n+-+-+-+-+-+-+-+-+-Terima Kasih telah menggunakan program kami :)+-+-+-+-+-+-+-+-+-+\n| '+' '*80+'|\n+-+-+-+-+-+-+-+-+-+-+-+-+ Created By : Hamdi R. +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')
        else:
            print('\nMohon masukkan pilihan yang sesuai\n')
            self.Bye()

Board_object=Board(0)
Board_object.run()