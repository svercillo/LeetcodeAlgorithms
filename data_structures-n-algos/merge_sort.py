def merge_sort(arr):
    n = len(arr)
    
    if len(arr) in [0, 1]:
        return arr
    

    larr = merge_sort(arr[:n//2])
    rarr = merge_sort(arr[n//2:])


    
    
    res = []
    lp, rp = 0, 0
    while lp < len(larr):

        while rp < len(rarr) and rarr[rp] < larr[lp]:
            res.append(rarr[rp])
            rp += 1

        res.append(larr[lp])
        lp += 1

    while lp < len(larr):
        res.append(larr[lp])
        lp += 1 


    while rp < len(rarr):
        res.append(rarr[rp])
        rp += 1

    return res


arr = [5,1,1,2,0,0]

res = merge_sort(arr)

print(res)