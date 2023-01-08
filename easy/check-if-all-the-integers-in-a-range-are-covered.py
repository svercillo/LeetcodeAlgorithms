class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s = set({})
        
        for r in ranges:
            for i in range(r[0], r[1] +1):
                s.add(i)
        
        for i in range(left, right+1):
            if i not in s:
                return False
            
        return True 
