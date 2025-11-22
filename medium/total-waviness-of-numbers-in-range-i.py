class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def calc(s):
            count = 0
            for i in range(1, len(s)-1):
                bd = int(s[i-1])
                d = int(s[i])
                ad = int(s[i+1])

                if bd < d > ad or  bd > d < ad:
                    count += 1
            return count
        count = 0
        for e in range(num1, num2+ 1):
            count += calc(str(e))
        return count
    ©leetcode
