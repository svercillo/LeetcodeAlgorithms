from bisect import bisect_left

class Solution:
    def maximizeTheProfit(self, n, offers): 
        offers.sort(key = lambda offer: (offer[0], offer[2]))
              
        # Question? what is the max profix that you could get for up to "i" homes?

        ''''
        1 <= n <= 10^5
        1 <= offers.length <= 10^5
        offers[i].length == 3
        '''
    
        def find_next_ind(array, target, start):
            fn = lambda x : x[0]
            n = len(array)
            if n == 1:
                return 0 if fn(array[0]) >= target else 1

            l, r = start, n - 1
            while l <= r:
                m = (l + r) // 2
                # print(m, (l, r))

                if m == 0:
                    if fn(array[0]) >= target: 
                        return 0
                    elif fn(array[1]) >= target: 
                        return 1
                    else: 
                        return 2
                    
                if fn(array[m-1]) < target:
                    if fn(array[m]) >= target:         
                        return m
                    else:
                        l = m + 1
                else:
                    r = m - 1
            
            if l == 0:
                if fn(array[0]) >= target: 
                    return 0
                elif fn(array[1]) >= target: 
                    return 1
                else: 
                    return 2
            
            m = l 
            # print(m)
            if fn(array[m-1]) < target:
                if m == len(offers) or fn(array[m]) >= target:         
                    return m
                else:
                    return m + 1
            else:
                return m -1
                        
                            

        @cache
        def maxProfit(i):
            # i == index in offers
            if i >= len(offers):
                return 0
            
            _max = 0
            _, end, profit = offers[i]
            
            # IF YOU DON'T TAKE THE OFFER
            _max = maxProfit(i + 1)

            # IF YOU DO TAKE THE 'i'th OFFER
            # find ind of next start geq current end
            next_start_ind = find_next_ind(offers, end+1, i + 1)

            # print((i, next_start_ind))
            _max = max(_max, maxProfit(next_start_ind) + profit)
            
            return _max
        
    
        return maxProfit(0)
