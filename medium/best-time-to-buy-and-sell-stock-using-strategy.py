class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        
        runningmoney = []
        runningmoneyw = []
        _sum = 0
        _sumw = 0
        for i, tup in enumerate(zip(prices, strategy)):
            p, s = tup
            _sum += p 

            runningmoney.append(_sum)

            if s == 1:
                _sumw += p
            elif s == -1:
                _sumw -= p


            runningmoneyw.append(_sumw)
        
        # print(runningmoney, runningmoneyw)

        result = runningmoneyw[-1]
        
        for k_start in range(len(prices) - k + 1):


            '''
            section1: until K normal 
            
            section3: from K -> normal
            '''

            
            section1  = runningmoneyw[k_start-1]  if k_start > 0 else 0

            section2 = runningmoney[k_start +  k - 1 ] - runningmoney[k_start +  int(k/ 2)  - 1 ] 
            


            section3 = runningmoneyw[-1] - runningmoneyw[k_start + k -1]

            # print([section1, section2, section3])

            # print(k_start, k )


            total = sum([section1, section2, section3])

            result = max(total, result)

        return result

    

            
            
