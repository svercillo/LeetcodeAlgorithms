class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ""
        for n in num: 
            s += str(n)
        
        return [int(c) for c in str(int(s) + k)]
        
            
