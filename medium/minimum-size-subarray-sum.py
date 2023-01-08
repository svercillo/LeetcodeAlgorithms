import math
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        
        n = len(nums)
        start = 0
        end = 0
        
        
        min_size = math.inf
        s = nums[0]
        while start < n: 

            print(start, end, s)
            
            if s < target: 
                end +=1 
                if end >= n:
                    break
                s += nums[end]
            else:
                if end -start +1 < min_size:
                    min_size = end-start+1
                
                if start == end:
                    
                    end +=1
                    if end >= n:
                        end -=1
                    else: 
                        s += nums[end]
                        
                    s -= nums[start]
                    start +=1 
                            
                else: 
                    s -= nums[start]
                    start +=1
                    
        return min_size if min_size != math.inf else 0
