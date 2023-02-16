class Solution:
    def minMaxGame(self, nums: List[int]) -> int:


        
        def recurse(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            new_nums = [0] * (n //2)
            for i in range(n //2):
                if i % 2 == 0:
                    new_nums[i] = min(nums[2*i], nums[2*i +1])
                else:
                    new_nums[i] = max(nums[2*i], nums[2*i +1])

            return recurse(new_nums)


        return recurse(nums)
        
