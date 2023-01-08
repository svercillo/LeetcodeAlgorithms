from collections import OrderedDict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = OrderedDict()
        counts[0] =0
        counts[1] =0
        counts[2] =0 
        
        for n in nums:
            counts[n] +=1
            
        print(counts)
        r = [] 
        i = 0 
        for c in counts: 
            for _ in range(counts[c]):
                nums[i] = c
                i +=1
