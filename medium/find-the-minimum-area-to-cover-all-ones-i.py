class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n , m = len(grid) , len( grid[0])

        istart, iend = math.inf, -math.inf
        mstart, mend = math.inf, -math.inf
        for i in range(n):
            count1s = 0
            for j in range(m):
                if grid[i][j]  == 1:
                    count1s += 1
            
            if count1s: 
                if istart == math.inf:
                    istart = i
                iend = i

            

            prerunning = 0
            sufrunning = 0
            start, end = -1, -1
            for j in range(m):
                prerunning += grid[i][j]
                sufrunning += grid[i][m-1 -j]

                if prerunning == count1s and end ==-1:
                    end = j

                if sufrunning == count1s and start == -1:
                    start = m-1 -j


            mstart = min(mstart, start)
            mend = max(mend, end)



        return (mend - mstart + 1)  *  (iend - istart + 1)
            
            
