class Solution:
    def searchRange(self, nums, target: int):
        
        
        # first check that element in arr
        if len(nums) == 0  or not self.binary_search(nums, 0, target)[1]:
            return [-1, -1]
        
        
        start_ind, _  = (-1, 0) if nums[0] == target else self.binary_search(nums, 0, target -0.5)
        end_ind, _ = self.binary_search(nums, 0, target + 0.5 )

        return [start_ind+1, end_ind]
        
    def binary_search(self, nums, start_ind, target): # start_ind is the ind of first element
            # print(nums, start_ind, target)
            if len(nums) == 1: 
                return start_ind, True if nums[0] == target else False
            
            
            if nums[len(nums) //2] == target:
                print(start_ind + len(nums) //2)
                return start_ind + len(nums) //2, True if nums[len(nums) //2] == target else False
            elif nums[len(nums) //2] < target: 
                return self.binary_search(nums[len(nums) //2:], start_ind + len(nums) //2, target)
            else: 
                return self.binary_search(nums[:len(nums) //2], start_ind, target)
            
