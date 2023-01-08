class Solution:
    def maximumSwap(self, num: int) -> int:
        values = [int(c) for c in str(num)]
        n = len(values)

        dp = [-1] * n # index of largest number to the right
        largest = -1
        largest_ind = -1
        for i in range(n-1, -1, -1):
            if values[i] > largest:
                largest = values[i]
                largest_ind = i
            dp[i] = largest_ind

        
        print(dp)
        for i in range(n):
            if dp[i] != -1 and values[i] != values[dp[i]]: 

                #swap
                t = values[i]
                values[i] = values[dp[i]]
                values[dp[i]] = t
                break # only swap once

        res = ""

        for v in values:
            res += str(v)

        return int(res)
