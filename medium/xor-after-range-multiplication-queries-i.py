class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 +7 

        for l, r, k, v in queries:
            while l <= r:
                nums[l] = (nums[l] * v)  % mod
                l += k

        res = 0
        for e in nums:

            res ^= e

        return res
