class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        res = [[1], [1,1]] 
        for i in range(1, numRows-1):
            row = [1]
            
            last = res[-1]
            
            for j in range(len(last) -1):
                row.append(last[j] + last[j+1])
                
            row.append(1)
            
            res.append(row)
            
        return res
            
