class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        
        score = 0
        highest_ind = 0
        for i, e in enumerate(nums):
            if e > nums[highest_ind]:
                score += (i - highest_ind) * nums[highest_ind]
                highest_ind = i



        score += (len(nums) -1 - highest_ind) * nums[highest_ind]

        return score


