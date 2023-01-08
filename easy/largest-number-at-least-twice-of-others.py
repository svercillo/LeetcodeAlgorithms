class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        _max = -1
        _smax = -1
        mind = -1
        
        for i in range(len(nums)):
            if nums[i] >= _max:
                _smax = _max
                _max = nums[i] 
                mind = i
            elif nums[i] > _smax:
                _smax = nums[i]
                
        
        if _max >= 2*_smax:
            return mind
        return -1
