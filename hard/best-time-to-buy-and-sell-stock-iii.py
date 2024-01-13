import math
class Solution:
    def maxProfit(self, prices) -> int:
        ''' 
        ideas: 
        
            reduce to only increasing peak/ valley 
            now the problem is how to combine these ranges to have a most two 10^5 
            if i can answer max(i, j) then I can easily solve this?
            if can answer profit(0, j) and profit(j+1, n) in O(1) 
                then can iterate through peak/valley array: 


            solution: pre calc profit(0,j) profit(j+ 1, n) for all valid j
        '''
        sunruns = self.get_sunruns(prices)

        print("Sunruns: ", sunruns)

        profit_prefix = self.get_profit_prefix(sunruns)
        profit_suffix = self.get_profit_suffix(sunruns)

        print("Prefix profit: ", profit_prefix)
        print("Suffix profit: ", profit_suffix)


        mprofit = 0
        for i in range(len(sunruns)-1):

            mprofit = max(
                mprofit,
                profit_prefix[i] + profit_suffix[i+1]
            )
            

        if len(profit_prefix): 
            mprofit = max(
                mprofit,
                profit_prefix[-1]
            )
        return mprofit



    def get_profit_prefix(self, sunruns):
        if not len(sunruns): 
            return []
        prefix = [None] * len(sunruns) 
        prefix[0] = sunruns[0][1] - sunruns[0][0]
        
        localmin = sunruns[0][0]
        localmax = sunruns[0][1]
        for index, (valley, peak) in enumerate(sunruns[1:]):
            i = index + 1

            if valley < localmin:
                localmin = valley
                localmax = peak

            elif peak > localmax:
                localmax = peak
            

            prefix[i] = max(localmax - localmin, prefix[i-1])

        return prefix
    

    def get_profit_suffix(self, sunruns):
        if not len(sunruns): 
            return []
        suffix = [None] * len(sunruns) 
        suffix[-1] = sunruns[-1][1] - sunruns[-1][0]
        
        localmin = sunruns[-1][0]
        localmax = sunruns[-1][1]
        for i in range(len(sunruns) -2, -1, -1):
            valley, peak = sunruns[i]
            
            
            if peak > localmax:
                localmax = peak
                localmin = valley
            elif valley < localmin:
                localmin = valley
            

            suffix[i] = max(localmax - localmin, suffix[i+1])

        return suffix

    def get_sunruns(self, prices):
        localmax = math.inf
        localmin = math.inf
        
        sunruns = []
        for p in prices:
            if p < localmax:
                if localmin < math.inf and localmin < localmax:
                    sunruns.append((localmin, localmax))
                localmin = p
                localmax = p
            else: 
                localmax = p

        if localmin < math.inf and localmin < localmax:
            sunruns.append((localmin, localmax))

        return sunruns
