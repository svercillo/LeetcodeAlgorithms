class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:

        if len(nums) == 1: 
            return True
        presum = 0
        postsum = 0

        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n

        total = sum(nums)

        for i in range(n): 
            presum += nums[i]
            postsum += nums[n-1-i]

            prefix[i] = presum
            postfix[n-1-i] = postsum
        
        nsplits = m - 1


        # print(prefix, postfix)

        def validSubarraySum(i, j):

            preval = 0 if i == 0 else prefix[i -1]
            postval = 0 if j == n-1 else postfix[j+1]
            subarraysum = total - preval - postval
            return subarraysum >= m

            # print(nums[i:j+1])
            # return sum(nums[i:j+1]) >= m
                


        @cache
        def canSplit(i, j):
            

            # print("array", nums[i:j+1])
            if j - i == 1:
                return True

            for t in range(i+1, j):
                if validSubarraySum(i, t) and canSplit(i, t) or validSubarraySum(t, j) and canSplit(t, n-1):
                    return True


            return False

        return canSplit(0, n-1)
