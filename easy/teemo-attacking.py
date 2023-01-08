class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        n = len(timeSeries)
        
        total_time =0 
        i =0
        while i < n:
            
            j = i + 1
            print(i )
            entered = False
            while j < n and timeSeries[j] < timeSeries[j -1] + duration: 
                entered = True
                j += 1

            if entered: 
                total_time += timeSeries[j -1 ] - timeSeries[i] 

            i = j 
            total_time += duration
        
                
                
                
        return total_time 
            
            
