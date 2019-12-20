def changeMe(arr):
    dicti={}
    for i in range(len(arr)) :
        if len(arr[i]) != 4 or arr[i][3] > 2018 :
            if len(arr[i]) != 4 :
                arr[i].append('invalid')
            else :
                arr[i][3] = 'invalid'
    for i in range(len(arr)):
        print(str(i+1)+" "+arr[i][0]+" "+arr[i][1]+" : ")
        if type(arr[i][3]) == int :
            dicti.update({'firstname': arr[i][0], 'lastname': arr[i][1], 'gender': arr[i][2], 'age': (2019-arr[i][3])})
        elif type(arr[i][3]) == str :
            dicti.update({'firstname': arr[i][0], 'lastname': arr[i][1], 'gender': arr[i][2], 'age': arr[i][3]})
        print(dicti)

changeMe([['Christ', 'Evans', 'Male', 1982], ['Robert', 'Downey', 'Male']])
