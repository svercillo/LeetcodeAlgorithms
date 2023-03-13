class Solution:
    def maxScore(self, nums: List[int]) -> int:

        nums.sort(reverse=True)


        mscore = 0

        presum = 0
        for e in nums: 
            presum += e
            if presum > 0:
                mscore += 1

        return mscore

