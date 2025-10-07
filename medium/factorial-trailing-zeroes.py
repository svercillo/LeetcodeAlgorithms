class Solution:
    def trailingZeroes(self, n: int) -> int:
        # is a function of 5 and 2s 

        powerof5 = 1
        res = 0
        while 5 ** powerof5 <= n:
        
            res += n // 5 ** powerof5

            powerof5 += 1         

        return res
