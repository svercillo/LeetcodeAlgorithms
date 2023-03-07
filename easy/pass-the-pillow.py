class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        pos = time % (n + n -2)

        if pos < n:
            return pos + 1

        return n - (pos - (n -1) )

        
