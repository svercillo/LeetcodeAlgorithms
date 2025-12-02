class Solution:
    def maximumEnergy(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def menergy(ind):
            if ind >= n:
                return 0
            return nums[ind]  + menergy(ind + k)
        
        total = -math.inf
        for i in range(n):
            total = max(total, menergy(i))

        return total
