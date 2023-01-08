class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas )
        diff = []
        for i in range( n):
            diff.append(gas[i] - cost[i])
                            
        
        last_start = -1
        start = 0
        while start <n:
            if diff[start] < 0:
                start +=1 
                continue
            
            running = 0
            running = diff[start]
            end = start +1 
            if end == n:
                end = 0
            running += diff[end]
                
            while end != start and running >= 0:
                end +=1 
                if end == n:
                    end = 0
                running += diff[end]
                
            if running >= 0:
                return start
            else: 
                if end < start:
                    break
                else:
                    start = end  
        
        return -1
