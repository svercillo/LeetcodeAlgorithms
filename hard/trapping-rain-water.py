class Solution:
    def trap(self, height: List[int]) -> int:
        forwards = [None] * len(height)
        backwards = [None] * len(height)
        # water_level = [None] * len(height)
        
        
        _max = -1
        for i in range(len(height)):
            if height[i] > _max:
                _max = height[i]
            forwards[i] = _max
            
        _max = -1
        for i in range(len(height)-1, -1, -1):
            if height[i] > _max:
                _max = height[i]
            backwards[i] = _max

        total = 0 
        for i in range(len(height)):
            water_level = min(forwards[i], backwards[i])
            
            total += water_level - height[i]
            
    
        
        return total 
        
