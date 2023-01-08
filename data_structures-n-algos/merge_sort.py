def mergesort(arr):
    def merge(arr1, arr2):
        p1, p2, n, m = 0, 0, len(arr1), len(arr2)
        res = []
        while p1 < n and p2 < m:
            if arr1[p1] <= arr2[p2]:
                res.append(arr1[p1])
                p1 +=1
            else:
                res.append(arr2[p2])
                p2 +=1 


        while p1 < n:
            res.append(arr1[p1])
            p1 +=1

        while p2 < m:
            res.append(arr2[p2])
            p2 += 1

        return res
    
    n = len(arr)    
    
    l, r = 0, n

    if n <= 1:
        return arr

    m = (l + r) //2

    larr = mergesort(arr[:m])
    rarr = mergesort(arr[m:]) 

    return merge(larr, rarr)


arr = [5,1,1,2,0,0]

res = mergesort(arr)

print(res)