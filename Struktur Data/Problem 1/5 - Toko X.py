import pprint

def countProfit(shippers):
    listBarang = [
    ['Sepatu Stacattu', 1500000, 10],
    ['Baju Zoro', 500000, 2],
    ['Sweater Uniklooh', 175000, 1]
    ]
    output = []

    a = {'product': 'Sepatu Stacattu'}
    asep = {'shoppers': []}
    leftsep = {'leftOver': 10}
    totalprofsep = {'totalProfit': 0}

    b={'product': 'Baju Zoro'}
    abaj = {'shoppers': []}
    leftbaj = {'leftOver': 2}
    totalprofbaj = {'totalProfit': 0}

    c={'product': 'Sweater Uniklooh'}
    aswe = {'shoppers': []}
    leftswe = {'leftOver': 1}
    totalprofswe = {'totalProfit': 0}

    for i in range(len(shippers)):
        if shippers[i]['product'] == 'Sepatu Stacattu':
            if shippers[i]['amount'] <= leftsep['leftOver'] :
                asep['shoppers'].append(shippers[i]['name'])
                leftsep['leftOver']=leftsep['leftOver']-shippers[i]['amount']
                totalprofsep['totalProfit']=totalprofsep['totalProfit']+(listBarang[0][1]*shippers[i]['amount'])
        elif shippers[i]['product'] == 'Baju Zoro':
            if shippers[i]['amount'] <= leftbaj['leftOver'] :
                abaj['shoppers'].append(shippers[i]['name'])
                leftbaj['leftOver']=leftbaj['leftOver']-shippers[i]['amount']
                totalprofbaj['totalProfit']=totalprofbaj['totalProfit']+(listBarang[1][1]*shippers[i]['amount'])
        elif shippers[i]['product'] == 'Sweater Uniklooh':
            if shippers[i]['amount'] <= leftswe['leftOver'] :
                aswe['shoppers'].append(shippers[i]['name'])
                leftswe['leftOver']=leftswe['leftOver']-shippers[i]['amount']
                totalprofswe['totalProfit']=totalprofswe['totalProfit']+(listBarang[2][1]*shippers[i]['amount'])
        else :
            continue
    a['shoppers'] = asep['shoppers']
    a['leftOver'] = leftsep['leftOver']
    a['totalProfit'] = totalprofsep['totalProfit']
    output.append(a)

    b['shoppers'] = abaj['shoppers']
    b['leftOver'] = leftbaj['leftOver']
    b['totalProfit'] = totalprofbaj['totalProfit']
    output.append(b)

    c['shoppers'] = aswe['shoppers']
    c['leftOver'] = leftswe['leftOver']
    c['totalProfit'] = totalprofswe['totalProfit']
    output.append(c)
    return output

pprint.pprint(countProfit([
 {'name': 'Windi', 'product': 'Sepatu Stacattu', 'amount': 8},
 {'name': 'Vanessa', 'product': 'Sepatu Stacattu', 'amount': 10},
 {'name': 'Rani', 'product': 'Sweater Uniklooh', 'amount': 1},
 {'name': 'Devi', 'product': 'Baju Zoro', 'amount': 1},
 {'name': 'Lisa', 'product': 'Baju Zoro', 'amount': 1}
]))

# print(countProfit([{'name': 'Windi', 'product': 'Sepatu Naiki', 'amount': 5}]))
