class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        
        # can just dfs whole island?
        dirs = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0]
        ]

        n = len(grid1)
        m = len(grid1[0])
        visited = set()
        def isValidSubIsland(i, j):
            nonlocal n, m        

            if (i, j) in visited:
                return False

            visited.add((i,j))


            invalid = False
            if grid1[i][j] == 0:
                invalid = True
        

            for down, right in dirs:
                ti = i + down
                tj = j + right


                # if out of range
                if not (0 <= ti < n) or not (0 <= tj < m): 
                    continue
                
                if grid2[ti][tj] == 1 and (ti, tj) not in visited:
                    if not isValidSubIsland(ti, tj): 
                        invalid = True

            return not invalid
                        



        count = 0
        for i in range(n):
            for j in range(m):
                
                if grid2[i][j] == 1 and  isValidSubIsland(i, j): 
                
                    # print(i, j)
                    # print(visited)
                    count += 1 

        return count
