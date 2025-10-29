class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        count = 0
        last = None
        s = s.lower()
        for c in s: 

            if c != last and last != None: 
                count += 1
            last = c 

        return count
