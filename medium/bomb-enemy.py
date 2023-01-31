class Solution:

    class NumThings:
        def __init__(self,val):
            self.val = val
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:

        rows = {} # maps coords to num things in a row
        cols = {} # maps coords to num things in a col

        n, m = len(grid), len(grid[0])
        
        

        for i in range(n):
            num_things = self.NumThings(0)
            for j in range(m):
                if grid[i][j] == "W":
                    num_things = self.NumThings(0)
                else:
                    if grid[i][j] == "E":
                        num_things.val += 1
                    rows[(i, j)] = num_things

        
        for j in range(m):
            num_things = self.NumThings(0)
            for i in range(n):
                if grid[i][j] == "W":
                    num_things = self.NumThings(0)
                else:
                    if grid[i][j] == "E":
                        num_things.val += 1
                cols[(i,j)] = num_things

        largest_num = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "0":
                    tot_things = rows[(i,j)].val + cols[(i,j)].val
                    largest_num = max(largest_num, tot_things)

        return largest_num
