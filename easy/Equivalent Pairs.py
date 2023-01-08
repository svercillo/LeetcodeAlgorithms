import math
class Solution:
    def solve(self, nums):
        
        n = len(nums)

        group = {}

        for i, n in enumerate(nums):
            if n not in group:
                group[n] = [] 

            group[n].append(i)
        

        def factorial(a):
            res = 1
            for i in range(1, a):
                res *= i
            return res

        count = 0
        for k in group:
            if len(group[k]) > 1:
                nk = len(group[k])
                print(nk)
                count += math.comb(nk, 2)

                

        return count



                
        


