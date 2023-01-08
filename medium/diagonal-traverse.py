class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        
        up = True
        res = []
        row =0
        
        
        
        while row < n:
            i = row
            j = 0
            
            
            ele = []
            while i >=0 and j < m:
                ele.append(mat[i][j])    
                i -=1
                j +=1 
                
            
            if up:
                res.extend(ele)
            else: 
                res.extend(ele[::-1])
                
            up = not up
            row += 1 
            
        
        
        col = 1
        
        while col < m:
            i = n-1
            j = col 
            
            ele = []
            while i >=0 and j < m:
                ele.append(mat[i][j])    
                i -=1
                j +=1
                
            if up:
                res.extend(ele)
            else: 
                res.extend(ele[::-1])
            up = not up 
            col +=1 
    
        return res 
        
        
        
