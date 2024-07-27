class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)

        groups = []
        
        i = 0
        while i < n:
            
            start = i
            if s[i] == '1':
                while i < n  and s[i] == '1':
                    i += 1

                end = i
                groups.append(end-start)
            
            i += 1


        if len(groups) == 0:
            return 0     

        mnum = 0
        curr_sum = 0
        for g in groups[:-1]:
            curr_sum += g
            
            mnum += curr_sum


        if s[-1] == '0':
            curr_sum += groups[-1]
            mnum += curr_sum 


        return mnum
