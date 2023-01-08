import math
def findEarliestMonth(stockPrice):

    prefix = []
    suffix = []

    _sum = 0
    for n in stockPrice:
        _sum += n
        prefix.append(_sum)

    _sum = 0
    for n in stockPrice[::-1]:
        _sum += n
        suffix.append(_sum)
    
    suffix = suffix[::-1]


    n = len(stockPrice)
    for i in range(n):
        prefix[i] //= (i +1)


    for i in range(n-1 , -1 , -1):
        suffix[i] //= (n- 1 - i  +1 )

    mdiff = math.inf
    mmonth  = 0
    for i in range(n-1):
        diff = abs(prefix[i] -  suffix[i+1])
        if diff < mdiff: 
            mdiff = diff
            mmonth = i +1
    
    return mmonth

    
        
res = findEarliestMonth([1])

print(res)


