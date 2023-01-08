def rev_binary_search(array, target):
    if len(array) == 0:
        return -1, False

    n = len(array)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        if array[m] == target:
            l = m
            break
        elif array[m] < target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n

    while array[l] <= target and l >= 0:
        l -= 1

    if l + 1 < len(array) and array[l + 1] == target:
        return l + 1
    else:
        return l


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        
        n, m = len(mat), len(mat[0])
        
        res = []
        
        for i in range(n):
            soldiers = rev_binary_search(mat[i], 0)
            res.append((soldiers, i))
                
                
                
        print(res)
        
        return [c[1] for i, c in enumerate(sorted(res, key = lambda k : k[0])) if i < k ]
                
