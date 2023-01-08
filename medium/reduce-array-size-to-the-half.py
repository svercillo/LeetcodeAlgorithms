import math
class Solution:
    def minSetSize(self, arr) -> int:
        HALF = math.ceil(len(arr)/2)
        d = {}
        for e in arr:
            if e in d: 
                d[e] += 1
                
            else: d[e] =1
            
        arr = []
        
        for k in d: 
            arr.append(d[k])
        
        arr.sort(reverse=True)

        print(arr)
        n = len(arr)
        
        running = 0
        for i in range(n):
            if running >= HALF:
                return i
            else: 
                running += arr[i]
        
        if running >= HALF:
            return n
