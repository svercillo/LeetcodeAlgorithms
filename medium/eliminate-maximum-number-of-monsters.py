class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        q = []
        n = len(dist)
        for i in range(n):
            q.append(dist[i] / speed[i])
            
        q.sort()
        
        
        
        currtime = 0
        for time in q:
            
            if currtime >= time:
                return currtime 
            currtime += 1
            
        return n
