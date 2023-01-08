class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        prefix, suffix = [], []
        
        s = 0
        for n in nums: 
            s += n
            prefix.append(s)
            
        s = 0
        for n in nums[::-1]: 
            s += n
            suffix.append(s)
        
        suffix = suffix [::-1]
        
        # if prefix[-1] == 0: 
        #     return 0
            
        for i in range(len(prefix)):
            
            lsum = 0
            rsum = 0
            if i>=1:
                lsum = prefix[i-1]
                
            if i< len(nums) -1:
                rsum = suffix[i+1]
            
            # print(lsum, rsum)
            if rsum == lsum:
                return i
        
        return -1     
