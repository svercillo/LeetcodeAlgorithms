class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        freq = {}
        for e in nums:
            if e not in freq:
                freq[e] = 0
            freq[e] += 1 

        
        
        res = 0
        for e in freq:
            v = freq[e]
            if v > 1:
                res += (v - 1) *(v) / 2
        
        return int(res)