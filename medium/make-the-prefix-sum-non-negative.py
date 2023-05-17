class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int: 
        

        mins = []
        count = 0        
        prefix = 0
        for i,e in enumerate(nums):
            prefix += e

            if e < 0:
                heapq.heappush(mins, e)

            if prefix < 0:
                prefix -= heapq.heappop(mins)
                count += 1

        
        return count
