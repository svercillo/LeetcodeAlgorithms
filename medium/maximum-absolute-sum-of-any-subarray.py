class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        

        # sliding window, only take the values that increase
        def maxSum(nums):
            mValue = 0
            currSum = 0
            l = 0
            n = len(nums)
            for r in range(n):
                
                currSum += nums[r]

                while currSum < 0:
                    currSum -= nums[l]
                    l += 1

                
                if currSum > mValue:
                    mValue = currSum

            return mValue

        return max(maxSum(nums), maxSum([-e for e in nums]))



