class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        MOD = 10 ** 9 + 7 
        
        @cache
        def getlargest(i,j):
            e = grid[i][j] 
            if i == n-1 and j == m-1:
                return (e, e)


            ps = []
            ns = []
            if i +1< n:
                p1, n1 = getlargest(i + 1, j)
                ps.append(p1)
                ns.append(n1)
                
            if j +1 < m:
                p2, n2 = getlargest(i, j+ 1)
                ps.append(p2)
                ns.append(n2)

            res= sorted([e * max(ps), e * min(ns)], reverse= True)

            return res
        
        containszero = False
        for i in range(n): 
            for j in range(m):
                if grid[i][j] == 0:
                    containszero = True
                    
        res = getlargest(0,0)[0]

        if res < 0:
            return 0 if containszero else -1
        return res % MOD
