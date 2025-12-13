class Solution:
    def smallestFactorization(self, num: int) -> int:
        # each prime factor has to be < 10

        mdigits = ceil(log(2 ** 32))
        factors = []

        if num == 1:
            return 1

        while num > 1:
            hasfactor = False 
            for f in range(9, 0, -1): 
                if num % f == 0:
                    factors.append(f)
                    num //= f

                    hasfactor = True
                    break
            if not hasfactor or len(factors) > mdigits: 
                return 0


        carr = []
        for i in range(len(factors) -1, -1, -1):
            carr.append(str(factors[i]))

        res = int("".join(carr))
        if res >= 2 ** 31:
            return 0

        return res


        
