class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # pointers?  

        n = len(nums)
        i =  0
        j = 0 


        while j < n: 
            nums[i] = nums[j]


            v = nums[j]
            c = j
            while j < n and nums[j] == v:
                if j -c == 1:
                    nums[i+ 1] = nums[j]
                    i += 1
                
                j += 1
        
            i += 1


        
        return i

