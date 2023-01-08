class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        
        for _ in range(len(s)):
            
            if s == goal:
                return True
            s = s[1:]+ s[0]
        
        return False
