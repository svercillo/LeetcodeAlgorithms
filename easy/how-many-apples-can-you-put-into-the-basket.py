class Solution:
    def maxNumberOfApples(self, weight) -> int:
        weight.sort()
        
        n = len(weight)
        load = 0
        i = 0
        while i < n and load <= 5000:
            load += weight[i]
            i+=1
            
        
        return i - 1 if i < n or load > 5000 else n
