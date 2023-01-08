def binary_search(array, target):
    if len(array) == 0:
        return None, False

    n = len(array)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        if array[m] == target:
            while m < n  and array[m] == target:
                m +=1

            return m -1, True
        elif array[m] > target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n - 1, False
    while array[l] > target and l >= 0:
        l -= 1

    return l, False

class Solution:
    def maxProfitAssignment(self, diff, profit, worker) -> int:
        n = len(diff)
        info = sorted(zip(diff, profit), key = lambda k : k[0])
        diff = [a[0] for a in info] 
        
        max_per_diff = []
        curr_max = 0
        for i in range(n):
            curr_max = max(info[i][1], curr_max)
            max_per_diff.append(curr_max)
            
        
        total = 0
        for ability in worker:
            ind, found = binary_search(diff, ability)

            if ind == -1:
                continue            
            total += max_per_diff[ind]
                      
        return total
