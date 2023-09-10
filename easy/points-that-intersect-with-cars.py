class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        dp = [0] * 102
        for start, end in nums:
            dp[start] += 1
            dp[end+1 ] -= 1

        count = 0

        running_sum = 0
        for i in range(101):
            running_sum += dp[i]

            if running_sum > 0:
                count += 1

        return count 





