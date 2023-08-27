class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        
        left =0
        right = 0
        _any = 0
        mdist = 0
        for c in moves:
            if c == "L":
                left += 1
            elif c == "R":
                right += 1
            else:
                _any += 1
            
            
            mdist = max(left + _any - right, right + _any- left)
            
        return mdist
            
                
