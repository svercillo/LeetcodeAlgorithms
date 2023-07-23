class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        res = []
        for word in words:
            last = []
            for c in word:
                if c == separator:
                    if len(last):
                        res.append("".join(last))
                    last = []
                else:
                    last.append(c)
                    
            if len(last):
                res.append("".join(last))
                
        
        return res 
            
