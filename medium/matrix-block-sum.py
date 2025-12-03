class Solution:
    def matrixBlockSum(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n ,m = len(grid), len(grid[0])
        
        x_prefix = []

        for i in range(n): 
            prefix = []
            running = 0
            for j in range(m):
                running += grid[i][j]
                prefix.append(running)
            x_prefix.append(prefix)

        res = []
        for i in range(n):
            row = [] 
            for j in range(m):


                total = 0
                for i_start in range(max(i - k, 0), min(i + k + 1, n)):
                    prefix = x_prefix[i_start]
                    
                    pre_start = prefix[j-k-1] if j - k -1  >= 0 else 0
                    pre_end = prefix[j+k] if j + k < m else prefix[-1]
                    total += pre_end - pre_start    
                
                row.append(total)
            res.append(row)

        return res



                
