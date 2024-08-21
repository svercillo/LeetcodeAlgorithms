class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:

        def function():
            nonlocal s, k
    
            l, r = 0, 0
            n = len(s)

            total = 0
            ones = 0
            zeros = 0
            while r < n:
                if s[r] == '1':
                    ones += 1
                if s[r] == '0':
                    zeros += 1
                
                while ones > k and zeros > k:
                    if s[l] == '1':
                        ones -=1
                    else:
                        zeros -= 1
                    l += 1

                diff = r +1 - l
                total += diff
                
                r += 1
            return total

        res1 = function()
        return res1
