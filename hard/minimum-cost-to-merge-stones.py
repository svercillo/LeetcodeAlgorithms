class Solution:
    def mergeStones(self, stones, k: int) -> int:
        # states-> 1: start new array on starting ind, 2: dont sum
        
        n = len(stones)
        
        dp = []

        prefix = [] 
        s = 0
        for e in stones: 
            s +=e
            prefix.append(s)
        
        suffix = []
        s = 0
        for e in stones[::-1]:
            s +=e
            suffix.append(s)    
        suffix = suffix[::-1]
        print(suffix)
            
        total = sum(stones)
        print(total)
        def calcsum(start, end):
            nonlocal prefix, suffix, total
            s = 0
            if start >= 1: 
                s += prefix[start-1] 
            if end <= len(suffix)-1: 
                s += suffix[end]
            
            return total - s
        
        
        res = calcsum(1, 3)
        print(res)
        

Solution().mergeStones(stones = [3,2,4,1], k = 2)