class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        m = len(mat[0])
        
        
        dirs = [[0, 1], [1, 0], [1, 1], [1, -1]]
        
        visited = [set() for _ in range(4)]
        
        
        longest = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    for ind, v in enumerate(visited):
                        if (i, j) in v:
                            continue
                        
                        ti, tj = i, j
                        count = 0
                        while 0<= ti < n and 0<= tj < m and mat[ti][tj] == 1: 
                            v.add((ti, tj))    
                            ti += dirs[ind][0]
                            tj += dirs[ind][1]
                            count += 1
                        
                        longest = max(longest, count)  
        return longest  
                            
                            
                        
                
                    
