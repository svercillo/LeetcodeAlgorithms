from collections import defaultdict
from functools import cache 

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        n = len(nums)


        maxes = [0] * n        
        dp = []
        for _ in range(n):
            dp.append(defaultdict(lambda : 1))

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                
                dp[i][diff] = dp[j][diff] + 1


                maxes[i] = max(dp[j][diff] + 1, maxes[i])

        return max(maxes)

                
