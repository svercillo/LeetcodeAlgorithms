class Solution:
    def tribonacci(self, n: int) -> int:

        def tribonacci(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            elif num == 2:
                return 1
            else:
                return tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)


        return tribonacci(n)
