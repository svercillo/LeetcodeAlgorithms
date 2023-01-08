from math import ceil

class Solution:

    def fourSum(self, nums, target):
        res = set()
        nums.sort()
        print(nums)
        for i, e in enumerate(nums):
            if i < len(nums) - 3: 
                self.threeSum(nums, target - e, res, i + 1, e)

        return res

    def threeSum(self, nums, target, res, starting, first_element):
        print(target, res, starting, first_element)
        n = len(nums)
        b = starting
        while b < n-2:             
            temp_target = target - nums[b]
            l = b + 1 
            r = n -1
            while l < r:
                _sum = nums[l] + nums[r]
                if _sum == temp_target:
                    res.add((first_element, nums[b], nums[l], nums[r]))
                    l += 1
                elif _sum < temp_target:
                    l += 1
                else:
                    r -= 1
            b += 1 
        return res