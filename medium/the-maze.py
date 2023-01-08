class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        
        i, j = start
        
        dirs = [(1,0), (-1,0), (0, 1), (0,-1)]
        
        n = len(maze)
        m = len(maze[0])
        
        visited = set()
        
        ispossible = False
        def dfs(i, j):
        
            nonlocal visited, destination, dirs, ispossible
                        
            if (i,j) in visited or ispossible:
                return 
                        
            visited.add((i,j))

            if [i,j] == destination:
                ispossible = True
                return
    
            
            for up, right in dirs:
                ti = i
                tj = j
                

                while 0 <= ti < n and 0 <= tj < m and maze[ti][tj] != 1:
                    ti += up
                    tj += right

                ti -= up
                tj -= right

                dfs(ti, tj)

                    
        dfs(i, j)
        
        return ispossible
        

res = Solution().hasPath(
    maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
)

print(res)
