class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])


        @cache
        def largestInDir(i, j, isRight): 
            if isRight: 
                if j + 1 < m and grid[i][j+1]: 
                    return largestInDir(i, j + 1, isRight) + 1
            else: 
                # if not is right then is down
                if i + 1 < n  and grid[i+1][j]: 
                    return largestInDir(i +1, j , isRight) + 1 

            return grid[i][j]
    
        def largestSquare(i, j):
            lenRight = largestInDir(i,j, True)
            lenDown = largestInDir(i,j, False)

            for side in range(min(lenRight, lenDown), 0, -1):
                topRightLenDown = largestInDir(i, j + side -1, False)
                bottomLeftLenRight = largestInDir(i + side -1, j, True)

                if topRightLenDown >= side and bottomLeftLenRight >= side:
                    print(side, i, j)
                    return side ** 2

            return 0
                
        _max = 0
        for i in range(n):
            for j in range(m): 
                if not grid[i][j]:
                    continue
                    
                res = largestSquare(i, j)
                if res > _max:
                    _max =res

        return _max
                
