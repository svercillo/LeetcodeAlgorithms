class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        # idea: get product of a range i, j in constant time
        # using a monotonic stack, find the index that each element is the min from the left and right in 
                        
        lstack, rstack = [], []
        ldp = [-1] * n 
        rdp = [-1] * n 
        
        for i, e in enumerate(nums):
            while len(lstack) and lstack[-1][0] > e:
                ldp[lstack[-1][1]] = i
                lstack.pop()
            lstack.append([e, i])

        for i in range(n-1, -1, -1):
            e = nums[i]
            while len(rstack) and rstack[-1][0] > e:
                rdp[rstack[-1][1]] = i
                rstack.pop()
            rstack.append([e, i])
            
        mscore = 0
        for i, e in enumerate(nums):
            llimit, rlimit = rdp[i], ldp[i]
            
            
            
            if rlimit == -1:
                rlimit = n
            
            

            score = (rlimit -1 - (llimit +1) + 1) * e 
                
            if llimit+ 1 <= k <= rlimit -1:
                mscore = max(score, mscore)

        return mscore    
