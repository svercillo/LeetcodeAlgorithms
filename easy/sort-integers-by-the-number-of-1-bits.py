class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        return [y[0] for y in sorted( [ (x, (sum(1 for c in (bin(x)[2:]) if c == '1'))) for x in arr ], key = lambda k : (k[1], k[0]) )]
        
    
