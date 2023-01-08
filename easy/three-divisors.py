class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1: return False 
        
        c = 2
        for i in range(2,n):
            if n %i ==0:
                c+=1
            if c > 3: return False
        
        return c ==3
        
    
            
