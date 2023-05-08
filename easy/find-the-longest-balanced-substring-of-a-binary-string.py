class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        mvalue = 0
        num_zeros = 0
        num_ones = 0
        for i in range(len(s)):
            if s[i] == "0":
                if i > 0 and s[i-1] == "1":
                    mvalue = max(mvalue, min(num_zeros, num_ones) * 2)
                    num_zeros = 0
                    num_ones = 0                
                num_zeros += 1
            else:
                num_ones += 1
        mvalue = max(mvalue, min(num_zeros, num_ones) * 2)
        return mvalue


            
