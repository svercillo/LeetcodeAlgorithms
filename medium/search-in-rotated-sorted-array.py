class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1 and nums[0] == target: 
            return 0

        _min = 10**4 +1 
        _min_ind = -1
        
        for i in range(0, len(nums)):
            if nums[i] < _min:
                _min = nums[i]
                _min_ind = i
        

        def bin_search(nums, target, offset =0  ) -> int:
        
            
            l = 0
            r = len(nums) -1

            while l <= r:

                mid = (l + r) // 2

                if nums[(mid + offset) % len(nums)] == target:
                    return mid

                elif nums[(mid + offset) % len(nums)] < target: 
                    l = mid +1
                else:
                    r = mid -1

            return -1

        res = bin_search(nums, target, _min_ind)
        return -1 if res == -1 else (_min_ind + res) % len(nums)
