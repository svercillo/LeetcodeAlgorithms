class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        for row in image: 
            i = 0
            
            while i < len(row)/2:
                t = row[i]
                
                row[i] = 1 if row[len(row) -1 - i] == 0 else 0
                row[len(row) -1 - i] = 1 if t ==0 else 0  
                
                i +=1 
                
            
        return image
            
