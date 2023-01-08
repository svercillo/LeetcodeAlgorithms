class Solution:
    def dietPlanPerformance(self, nums: List[int], k: int, lower: int, upper: int) -> int:
        # sliding window
        
        q = deque()
        
        _sum = 0 
        points = 0
        
        n = len(nums)
        for i in range(n):
            q.append(nums[i])
            _sum += nums[i]
            
            if i >= k:
                left = q.popleft()
                _sum -= left
                
            if i >= k -1:
                if _sum < lower:
                    points -= 1
                    
                if _sum > upper:
                    points += 1
        
        return points
