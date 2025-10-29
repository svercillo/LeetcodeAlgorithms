class Solution:
    def clearDigits(self, s: str) -> str:
        
        n = len(s) 
        
        res = []
        num_digits = 0
        
        i = n -1
        while i >= 0:
            
            if s[i].isdigit():
                num_digits += 1
            else:
                
                if num_digits > 0:
                    num_digits -=1 
                else:
                    res.append(s[i])    
            i -= 1
        
    
        return "".join(res[::-1])
