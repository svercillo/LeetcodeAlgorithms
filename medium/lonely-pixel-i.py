class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        
        pic = picture
        n = len(pic)
        m = len(pic[0])
        
        rows = {}
        cols = {} 
        
        for i in range(n):
            for j in range(m):
                if pic[i][j] == "B":
                    if i not in rows:
                        rows[i] = 0
                    rows[i] +=1
                        
                    if j not in cols:
                        cols[j] = 0
                    cols[j] += 1
                   
        count = 0 
        for i in range(n):
            for j in range(m):
                if pic[i][j] == "B":
                    if rows[i] == 1 and cols[j] == 1:
                        count +=1 
                        
        return count
                        
                    
                
