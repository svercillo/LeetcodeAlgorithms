class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        n = len(costs)
        i = 0
        while i < n  and coins >= costs[i] > 0:
            coins -= costs[i]
            i += 1
            
        return i
            
