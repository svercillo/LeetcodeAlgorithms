# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        overflow = 2 ** 31 -1
        

        r = 1
        
        res = reader.get(r // 2)
        
        while res != overflow and res <= target:
            if res == target:
                return r // 2
            
            r *= 2
            res = reader.get(r // 2)
        
        def binary_search(n, target):
            nonlocal reader
            
            l, r = 0, n
            
            while l <= r:
                m = (l + r) // 2

                res = reader.get(m)

                if res == target:
                    return m, True
                
                elif res < target: 
                    l = m + 1
                else:
                    r = m - 1
                    
            if l == n:
                return  n-1, False
            
            while reader.get(l) > target and l >= 0:
                l -= 1
            
            return l, False
        
        ind, valid = binary_search(r, target) 
        if not valid:
            return -1
        
        return ind
