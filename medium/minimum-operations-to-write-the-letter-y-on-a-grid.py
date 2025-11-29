class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        yvals = {0: 0, 1:0, 2: 0}
        vals = {0: 0, 1:0, 2: 0}

        
        ycoords = set()
        for i in range(n// 2):
            print(i, i)
            yvals[grid[i][i]] += 1
            yvals[grid[i][n-1 - i]] += 1
            ycoords.add((i,i))
            ycoords.add((i,n-1-i))

        for i in range(n//2, n ):
            print(i, n//2)
            yvals[grid[i][n//2]] += 1
            ycoords.add((i, n//2))

        for i in range(n):
            for j in range(n):
                coords = (i,j)
                if coords in ycoords:
                    continue
                vals[grid[i][j]] += 1

        mflips = math.inf

        for ycolor in range(3):

            flipy = len(ycoords) - yvals[ycolor]

            for xcolor in range(3):
                if xcolor == ycolor: 
                    continue
                flipx = n * n - len(ycoords) - vals[xcolor]
        

                mflips = min(mflips, flipy + flipx)

        return mflips



        


                





        
        
