class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(s) < len(t): 
            return 0

        
        @cache
        def num_distinct(sind, tind):

            if tind == len(t):
                return 1

            elif sind == len(s):
                return 0                

            count = 0
            if s[sind] == t[tind]:
                count += num_distinct(sind+ 1, tind + 1)

            count += num_distinct(sind + 1, tind)

            return count
        
        return num_distinct(0, 0)
