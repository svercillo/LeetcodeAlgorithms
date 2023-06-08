class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        # idea bfs
        comp_color = grid[row][col]
        q = [(row, col)]

        dirs = [
            [1,0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        to_add = set()
        n, m = len(grid), len(grid[0])
        visited = set() 
        while len(q):
            new_q = []
            for i, j in q:
                if (i, j) in visited:
                    continue
                visited.add((i,j))
                
                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if 0 <= ti < n and 0 <= tj < m:
                        if grid[ti][tj] != comp_color:
                            to_add.add((i, j))
                        else:
                            new_q.append((ti, tj))

                    else:
                        to_add.add((i, j))
            q = new_q

        for i, j in to_add:
            grid[i][j] = color

        return grid
  
