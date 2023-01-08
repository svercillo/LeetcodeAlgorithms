from bisect import bisect_left


class Solution:
    def missingElement(self, nums, k: int) -> int:
        n = len(nums)

        dp = [0] * n
        starting = nums[0]

        total_sum = 0
        for i in range(n - 1):
            total_sum += nums[i + 1] - nums[i] - 1
            dp[i + 1] = total_sum

        print(dp, k)
        ind = bisect_left(dp, k)

        if ind >= n:
            return nums[-1] + k - dp[-1]

        return nums[ind - 1] + k - dp[ind - 1]


nums = [1, 2, 4]
k = 3

res = Solution().missingElement(nums, k)

print(res)
