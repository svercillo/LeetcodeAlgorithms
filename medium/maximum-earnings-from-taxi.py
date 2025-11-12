class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        print(rides)

        def nxtride(value):
            l,  r = 0, len(rides)
            while l < r:
                m = (l + r) // 2
                if rides[m][0] < value:
                    l = m + 1
                else:
                    r = m
            return l

            
        @cache
        def mearnings(ind): 
            if ind >= len(rides) or rides[ind][1] > n:
                return 0
            
            start, end, tip = rides[ind]
            return max(
                mearnings(nxtride(end)) + end - start + tip, # take 
                mearnings(ind + 1)  # don't take
            )

        return mearnings(0)
            




            
