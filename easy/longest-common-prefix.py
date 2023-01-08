class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        _min = 201
        for s in strs:
            if len(s) < _min:
                _min = len(s)
        p = 0
        
        while p < _min:
            
            exit = False 
            c = strs[0][p]
            for w in strs:
                if w[p] != c:
                    exit =True 
                    break
            
            if exit: break
                        
            p +=1 
        
        return strs[0][:p]
