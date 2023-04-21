class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisors.sort()
        mcount = -1
        mcount_d = -1
        for d in divisors:
            count = 0
            for e in nums:
                if e % d == 0:
                    count += 1

            
            if count > mcount:
                mcount = count
                mcount_d = d

        
        return mcount_d
                    
