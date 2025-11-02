class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)

        # take all zeros 
        # take ones in rev order until I can't


        ones = []
        prefix = [0] * n
        running = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == '0':
                running += 1
            else:
                ones.append(i)
            prefix[i] = running

        
        numones = 0
        value = 0
        ind = 0
        while ind < len(ones) and value + 2 ** (prefix[ones[ind]] + numones) <= k:
            value += 2 ** (prefix[ones[ind]] + numones)
            print(ones[ind], value, numones)
            numones += 1
            ind+= 1

            
    

        return numones + prefix[0]
        print(prefix, ones, value)
        


        
        
