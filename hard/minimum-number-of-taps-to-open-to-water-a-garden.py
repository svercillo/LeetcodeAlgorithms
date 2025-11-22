from heapq import heappush
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''
        idea: 
            garden needing to get gardened, choose the furthest point always
                min heap of ready intervals 
                if ind > min heap take off the ready intervals
                keep a max for the number i can jump to
        '''

        checkpoint = [-1] * (n + 1)

        for i, v in enumerate(ranges):
            lower = max(i - v, 0)
            upper = i + v
            checkpoint[lower] = max(checkpoint[lower], upper)


        running = 0
        for i in range(n+1):
            running = max(checkpoint[i], running) 
            checkpoint[i] = running
        
        print(checkpoint)


        jumps = 0
        ind = 0 
        while ind < n:
            if ind == checkpoint[ind]:
                return -1
            ind = checkpoint[ind]

            jumps += 1

        return jumps















        


        
        
