def binary_search(array, target):
    
    n = len(array)
    
    l, r = 0, n
    
    while l < r: 
        
        m = (l+r)//2
        
        # if array[m] == target:
        #     return m
        if array[m] > target:
            r = m
        else:
            l = m +1 

    return l
        
import random

import bisect

class Solution:
    sum = 0 
    start = []
    
    def __init__(self, w: List[int]):
        self.start.clear()
        print(w)
        for n in w:
            print(n)
            self.sum += n
            self.start.append(self.sum)
        
 
        self.n = len(w)


    def pickIndex(self) -> int:
        # print(self.start)
        res = self.sum * random.random()
        index = bisect.bisect(self.start, res, 0, self.n-1)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
