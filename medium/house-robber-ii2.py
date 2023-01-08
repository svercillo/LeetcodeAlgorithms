class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        second = nums.copy()
        second.pop(0)
        nums.pop()
        
        
        return max(self.helper(nums), self.helper(second))
    def helper(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n == 1: 
            return nums[0]
        elif n ==2:
            return max(nums[0], nums[1])

        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2,n):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return max(dp[n -1 ], dp[n-2])
