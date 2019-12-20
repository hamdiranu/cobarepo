def initialGroupingDescending(studentArr) :
    awalhrf=[]
    output=[]
    for i in studentArr:
        awalhrf.append(i[0])
    awalhrf=list(set(awalhrf))
    ganti = True
    while ganti == True:
        ganti = False
        for i in range(len(awalhrf)-1):
            vardumb=0
            if awalhrf[i+1]>awalhrf[i]:
                vardumb = awalhrf[i]
                awalhrf[i] = awalhrf[i+1]
                awalhrf[i+1] = vardumb
                ganti = True
    for i in awalhrf:
        new_list=[]
        new_list.append(i)
        for h in studentArr:
            if h[0]==i:
                new_list.append(h)
        output.append(new_list)
    return output
print('')
print(initialGroupingDescending(['Budi', 'Badu', 'Joni', 'Jono']))
'''
[
[ 'J', 'Joni', 'Jono' ],
[ 'B', 'Budi', 'Badu' ]
]
'''
print('')

print(initialGroupingDescending(['Mickey', 'Yusuf', 'Donald', 'Ali', 'Gong']))
'''
[
[ 'Y', 'Yusuf' ],
[ 'M', 'Mickey' ],
[ 'G', 'Gong' ],
[ 'D', 'Donald' ],
[ 'A', 'Ali' ]
]
'''
print('')
print(initialGroupingDescending(['Rock', 'Stone', 'Brick', 'Rocker', 'Sticker']))
'''
[
[ 'S', 'Stone', 'Sticker' ],
[ 'R', 'Rock', 'Rocker' ],
[ 'B', 'Brick' ]
]
'''
print('')