from math import log, floor, ceil
class Solution:
    def grayCode(self, n: int):
        poss = [i for i in range(2, n + 1)]
        
        res = [0, 1]

        def ispower2(x):
            return 0 <= ( log(x)/ log(2)) % 1 < 0.000001
        
        def numBits(x):
            return floor(log(x)/ log(2))
        
        
        def diffbybit(a, b):
            if a == b + 1 or a == b -1:
                return True

            if numBits(a) != numBits(b):
                return False

            if ispower2(a ^ b):
                return True
            else:
                return False





        def validSeq(poss, remaining): 
            last = remaining[-1]
            for e in poss:
                (last,e)








        return validSeq(tuple(poss), tuple(res))



Solution().grayCode(5) 