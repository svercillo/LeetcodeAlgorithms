class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:

        terminate = False
        
        @cache
        def dfs(i, j, numones):
            nonlocal terminate
            n,m = len(grid), len(grid[0])

            if terminate:
                return True

            numzeros = i + j + 1  - numones
            if i == n-1 and j == m-1:
                if numzeros == numones:
                    terminate = True
                    return True

            remaining = n - 1 - i + m - 1 - j
            if abs(numzeros - numones) > remaining:
                return False
            
            if grid[i][j] == 1:
                numones += 1
            
            valid_path = False
            if i + 1 < n:
                valid_path = valid_path or dfs(i+1, j, numones)
            
            if j + 1 < m:
                valid_path = valid_path or dfs(i, j+1, numones)
                
            return valid_path

        
        return dfs(0, 0, 0)