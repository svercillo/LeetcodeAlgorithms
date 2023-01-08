class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        n = len(logs)
        longest = 0
        longest_id = None 
        for i in range(n):
            
            if i == 0:
                start = 0
            else: 
                start = logs[i-1][1]
            
            leave_time = logs[i][1] - start
            
            if leave_time > longest:
                longest = leave_time
                longest_id = logs[i][0]
                
            elif leave_time == longest:
                longest_id = min(longest_id, logs[i][0])

        return longest_id            
