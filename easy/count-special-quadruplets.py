class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
    
        
        def recurse(index, placement, _sum):

            if index == len(nums):
                return 0
            
            if placement == 3:
                num_ways = 0
                if nums[index] == _sum: 
                    num_ways += 1

                num_ways += recurse(index + 1, placement, _sum)

                return num_ways
            else:

                num_ways = (    
                    recurse(index + 1, placement + 1, _sum + nums[index]) # take integer
                    + recurse(index + 1, placement, _sum) # don't take integer
                )

                return num_ways

                    
        return recurse(0, 0, 0)
                
