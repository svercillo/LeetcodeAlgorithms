from pprint import pprint 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = set()
        n, m = len(grid), len(grid[0])
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                elif grid[i][j] == 2:
                    q.append((i,j))

        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        time = 0
        print(q)
        while len(q):
            new_q = []
            for i,j in q:
                
                if (i, j) in fresh:
                    fresh.remove((i, j))