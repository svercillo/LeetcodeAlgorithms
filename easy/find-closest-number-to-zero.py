class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist = math.inf
        closest = 0
        for e in nums:
            if abs(e) < dist or (abs(e) == dist and e > closest):
                dist = abs(e) 
                closest = e

            
        return closest 
