import math
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:


        mdigits = math.ceil(math.log(n-2) / math.log(2)) + (1 if n-2 % 2 == 0 else 0)

        pow2 = [-1] * (mdigits +2)

        for i in range(mdigits + 2):
            pow2[i] = int(2 ** i)

        print(mdigits)

        
        for i in range(2, n-1):
            ndigits = math.ceil(math.log(n) / math.log(2)) + (1 if n % 2 == 0 else 0)


            if ndigits % 2 == 0:
                l = int(ndigits / 2)
                r = int(ndigits / 2 + 1)
            else:
                l = int(ndigits / 2)
                r = int(ndigits / 2)

            while l >= 0:
                print(l, r)
                print(pow2)
                if pow2[l]  & n != pow2[r] & n:
                    return False
                l -= 1
                r += 1

        return True
