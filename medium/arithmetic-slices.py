class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n # contains the number of arithmetic subarrays that start at index i

        if n < 3:
            return 0

        res = 0
        
        for i in range(2, n):
            diff1 = nums[i] - nums[i-1]
            diff2 = nums[i-1] - nums[i-2]

            if diff1 == diff2: # arithmetic subarray
                dp[i] += dp[i-1] + 1
            
            res += dp[i]

        print(dp)
        return res 
