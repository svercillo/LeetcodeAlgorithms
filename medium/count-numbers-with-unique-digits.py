class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = 0
        _round = 2
        num_digits = 10

        if n == 0:
            return 1

        def choose(n, r):
            return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
        while _round <=n:
            
            nCr = math.factorial(10) / math.factorial(10 - _round)

            print(f"choose {10}nCr{_round}", nCr)
            res += nCr / 10 * 9
            print(res)
            _round += 1

        return int(res + 10)

        
