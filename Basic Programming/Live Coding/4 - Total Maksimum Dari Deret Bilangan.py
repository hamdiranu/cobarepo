def totalList(lst):
    sum=0
    for j in range(len(lst)):
        sum+=lst[j]
    return sum

def maxSequence(arr):
    maxsum = float('-inf')
    lstmaxsum = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if totalList(arr[i:j+1])>maxsum:
                lstmaxsum = arr[i:j+1]
                maxsum=totalList(arr[i:j+1])
            else:
                continue
    return maxsum

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
print(maxSequence([-2, -5, 6, -2, -3, 1, 5, -6])) # 7
print(maxSequence([-2, -1, 1, 4, 5, 7, 8])) # 7
print(maxSequence([7, -8, 6, -2, -3, 1, 5, -6])) # 7


