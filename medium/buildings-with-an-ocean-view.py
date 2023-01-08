class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        n = len(heights)
        
        res = []
        highest = 0
        for i in range(n-1, -1 ,-1):
            if heights[i] > highest:
                res.append(i)
                highest = heights[i]
        
        return reversed(res)
            
