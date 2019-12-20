import pprint
def shoppingTime(memberId, money):
    barang = {'stacattu':1500000,'zoro':500000,'HnN':250000,'unik':175000,'casing':50000}
    out = {}
    if memberId == '' :
        return ('Mohon maaf, toko X hanya berlaku untuk member saja')
    else :
        if money == '' :
            return ('Mohon maaf, uang tidak cukup')
        else :
            out['memberId'] = memberId
            out['money'] = money
            listpur = []
            change = money
            if money >= barang['stacattu']:
                listpur.append('Sepatu Stacattu')
                change -= barang['stacattu']
                money -= barang['stacattu']
            if money >= barang['zoro']:
                listpur.append('Baju Zoro')
                change -= barang['zoro']
                money -= barang['zoro']
            if money >= barang['HnN']:
                listpur.append('Baju H&N')
                change -= barang['HnN']
                money -= barang['HnN']
            if money >= barang['unik']:
                listpur.append('Sweater uniklooh')
                change -= barang['unik']
                money -= barang['unik']
            if money >= barang['casing']:
                listpur.append('Casing Handphone')
                change -= barang['casing']
                money -= barang['casing']
                out['listPurchased'] = listpur
                out['changeMoney: '] = change
                return out
            else :
                return ('Mohon maaf, uang tidak cukup')


pprint.pprint(shoppingTime('1820RzKrnWn08', 2475000))
'''
{ memberId: '1820RzKrnWn08',
  money: 2475000,
  listPurchased:
   [ 'Sepatu Stacattu',
     'Baju Zoro',
     'Baju H&N',
     'Sweater Uniklooh',
     'Casing Handphone' ],
   changeMoney: 0 }
'''
print(' ')
pprint.pprint(shoppingTime('82Ku8Ma742', 170000))
'''
{ memberId: '82Ku8Ma742',
 money: 170000,
 listPurchased:
  [ 'Casing Handphone' ],
 changeMoney: 120000 }
'''
print(' ')
pprint.pprint(shoppingTime('', 2475000))
# Mohon maaf, toko X hanya berlaku untuk member saja
print(' ')
pprint.pprint(shoppingTime('234JdhweRxa53', 15000))
# Mohon maaf, uang tidak cukup
print(' ')
pprint.pprint(shoppingTime('', ''))
# Mohon maaf, toko X hanya berlaku untuk member saja
              

