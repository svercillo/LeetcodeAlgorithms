class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        abs_max = -9999999


        _min = nums[0]
        _max = nums[0]

        if _max > abs_max:
            abs_max = _max
        
        for i in range(1,n):
            l_max = _max
            l_min = _min

            print(l_max, l_min)
            _max = max(l_min * nums[i], l_max  * nums[i], nums[i])
            _min = min(l_max * nums[i], l_min  * nums[i], nums[i])
            
            
            if _max > abs_max:
                abs_max = _max
        
        return abs_max
