class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ''' 
        idea: 
            prefix / suffix sum?
        '''
        n = len(nums)
        run = 0
        prefix = [] 
        for e in nums:
            if e  == 1:
                run += e
            else:
                run = 0
            prefix.append(run)

        run = 0
        suffix = [] 
        for e in nums[::-1]:
            if e  == 1:
                run += e
            else:
                run = 0
            suffix.append(run)
        suffix = suffix[::-1]


        mvalue = 0
        for i in range(len(nums)):
            before = 0 
            if i >0:
                before = prefix[i-1]

            after = 0
            if i + 1< n:
                after = suffix[i+1]
            
            mvalue = max(mvalue, before +after)

        return mvalue
                
        
