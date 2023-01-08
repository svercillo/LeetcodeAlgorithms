class Solution:
    def toHexspeak(self, num: str) -> str:
        hstr = hex(int(num))[2:]
        
        
        hstr = hstr.replace("0", "O")
        hstr = hstr.replace("1", "I")
                
        valid = set(['A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'])

        carr = [c for c in hstr]
        for i,c in enumerate(hstr):
            if c.upper() not in valid:
                return "ERROR"
            else:
                carr[i] = c.upper()
                            
        return "".join(carr)
        
        
        
        
        
