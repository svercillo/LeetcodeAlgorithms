
import math
from functools import cache

# class Solution:
#     def minimumMoves(self, grid) -> int:
        
#         def serializeGrid(grid):
#             return tuple(tuple(row) for row in grid)

#         def deserializeGrid(grid): 
#             new_grid = []
#             for row in grid:
#                 new_row = []
#                 for e in row:
#                     new_row.append(e)
#                 new_grid.append(new_row)

#             return new_grid

#         dirs = [
#             [1, 0],
#             [-1, 0],
#             [0, 1],
#             [0, -1]
#         ]
    
#         grid = serializeGrid(grid)
#         path = set(grid)

#         @cache
#         def dfs(grid):
            
#             print(grid)
#             to_move = []
#             for i in range(3):
#                 for j in range(3):
#                     if grid[i][j] > 1:
#                         to_move.append((i, j, grid[i][j]))
#             if len(to_move) == 0: 
#                 return 0
                

#             to_move.sort(key=lambda k : -k[2])
#             possible = []
#             for i, j, _ in to_move:
#                 for down, right in dirs:
#                     ti = i + down
#                     tj = j + right

#                     if not (0 <= ti < 3 and 0 <= tj < 3):
#                         continue
                    
#                     new_grid = deserializeGrid(grid)
                    
                    
#                     new_grid[ti][tj] += 1
#                     new_grid[i][j] -= 1
                    
#                     serialized = serializeGrid(new_grid)
#                     if serialized in path:
#                         continue
                    
#                     path.add(serialized)
#                     res = dfs(serialized)
#                     if res == -math.inf:
#                         continue 
#                     possible.append(res + 1)
#                     path.remove(serialized)
            
#             if len(possible) == 0:
#                 return -math.inf
            
#             # print(possible)
#             return min(possible)
        
#         return dfs(grid)
    

class Solution:
    def __init__(self):
        self.ans = float('inf')

    def solve(self, i, a, b, vis, c, s):
        if c == len(b):
            self.ans = min(self.ans, s)
            return
        for j in range(len(b)):
            if vis[j] == 1:
                continue
            vis[j] = 1
            x = abs(a[i][0] - b[j][0]) + abs(a[i][1] - b[j][1])
            self.(i + 1, a, b, vis, c + 1, s + x)
            vis[j] = 0

    def minimumMoves(self, v):
        a = []
        b = []
        for i in range(3):
            for j in range(3):
                if v[i][j] == 0:
                    b.append([i, j])
                else:
                    x = v[i][j] - 1
                    t = [i, j]
                    while x > 0:
                        a.append(t.copy())
                        x -= 1

        print(a)
        x = len(b)
        vis = [0] * x
        self.ans = float('inf')
        self.solve(0, a, b, vis, 0, 0)
        return self.ans


res = Solution().minimumMoves([[0,2,1],[1,2,0],[3,0,0]])

print(res)
