class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        arr = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]
        
        
        res = []
        
        for w in words: 
            row = -1
            valid = True
            for c in w: 
                for i in range(len(arr)): 
                    if c in arr[i]:
                        if row == -1:
                            row = i
                        elif row != i:
                            valid = False
            if valid: 
                res.append(w)
                
        return res
                
                
                
