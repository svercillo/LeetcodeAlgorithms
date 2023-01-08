from math import comb


class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        num_ones = 0
        for c in s :
            if c == '1':
                num_ones +=1 
                
        if num_ones % 3 != 0: 
            return 0

        if num_ones == 0: 
            return comb(len(s)-1, 2) % (10 ** 9 + 7)

        
        
        req_ones = num_ones / 3
        num_ones = 0 
        
        zeros = []
        start = 0
        end = 0

        while end < n:
            c = s[end]

            if c == "1":
                num_ones += 1 
                if num_ones == req_ones: 
                    # print("SDfsdfd", start,  end)
                    
                    start = end
                    end +=1 

                elif num_ones > req_ones:
                    zeros.append((start, end))
                    num_ones = 1
                    start = end
                    end +=1 
                else: 
                    end += 1

            else :
                # print(start, end, num_ones, req_ones)
                end +=1

        # zeros.append((start,end))

        
        # print(zeros)
        res = 1 
        for z in zeros:
            res *= z[1] - z[0]

        return res % (10 ** 9 + 7)

        
            
