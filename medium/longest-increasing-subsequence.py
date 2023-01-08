class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-1] * n



        def recurse(i):
            nonlocal n
            if i == n -1:
                dp[i] = 1
                return 1

    
            longest_subseq = 0
            j = i + 1
            while j < n:
                if nums[i] < nums[j]:
                    longest_subseq = max(longest_subseq, dp[j])

                j += 1

            dp[i] = longest_subseq + 1
            return longest_subseq + 1

        
        res = 0
        for i in range(n-1, -1, -1):
            res = max(recurse(i), res)


        return res
