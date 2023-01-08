class Solution:
    def threeSum(self, nums):
        
        nums.sort()
        n = len(nums)
        b = 0
        res = set()
        while b < n-2: 
            
            target = - nums[b]
            l = b + 1 
            r = n -1

            while l < r:
                _sum = nums[l] + nums[r]

                if _sum == target:

                    res.add((nums[b], nums[l], nums[r]))
                    l += 1
                elif _sum < target:
                    l += 1
                else:
                    r -= 1
            b += 1 
        return res
