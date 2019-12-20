class Calculator:
    x =0
    y =0
    # =========================== Opening ===========================
    def run(self):
        print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ CALCULATOR +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')
        print('1: Open Calculator \n99: Exit\n')
        input1=int(input('Masukkan pilihan anda: '))
        if input1==1:
            self.inputval()
        elif input1==99:
            print('\n           Terima Kasih telah menggunakan program kami :)\n')
        else:
            print('\nMohon masukkan pilihan yang sesuai')
            self.run()
    # =========================== Input Value ===========================
    def inputval(self):
        self.x=input('\nMasukkan Value 1: ')
        self.x=float(self.x)
        self.y=input('Masukkan Value 2: ')
        self.y=float(self.y)
        self.main()
    # =========================== Pilihan ===========================
    def main(self):
        print('\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ CALCULATOR +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')
        print('1. Add Value \n2. Sub Value \n3. Multiply Value \n4. Divide Value\n')
        print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ CALCULATOR +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n')
        input2=int(input('Pilihan anda: '))
        if input2==1:
            self.Add()
        elif input2==2:
            self.Sub()
        elif input2==3:
            self.Mul()
        elif input2==4:
            self.Div()
        else:
            print('mohon masukkan bilangan bulat dalam interval 1-4')
            self.main()
    # =========================== Operasi Matematika ===========================
    def Add(self):
        print(self.x+self.y)
        self.Bye()

    def Sub(self):
        print(self.x-self.y)
        self.Bye()

    def Mul(self):
        print(self.x*self.y)
        self.Bye()

    def Div(self):
        if self.y != 0:
            print(self.x/self.y)
            self.Bye()     
        else:
            print ('Mohon masukkan nilai value 2 selain 0')
            self.y=int(input('Masukkan Value 2: '))
            self.Div()
    # =========================== Keluar ===========================
    def Bye(self):
        input3=input('\nIngin mencoba lagi? (Y/N) :')
        if input3=="Y" or input3=="y":
            self.run()
        elif input3=="N" or input3=="n":
            print('\n+-+-+-+-+-+-+-+-+-Terima Kasih telah menggunakan program kami :)+-+-+-+-+-+-+-+-+-\n')
        else:
            print('\nMohon masukkan pilihan yang sesuai')
            self.Bye()

calculator = Calculator()
calculator.run()