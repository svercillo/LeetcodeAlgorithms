class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
        def numRowsIfFirst(instances): 
            # 2 ( n (n + 1) / 2) - n = red 
            return math.floor(math.sqrt(instances))
        
        def numRowsIfSecond(instances): 
            # 2 ( n (n + 1) / 2) - blue = 0            
            # n*n + n - blue = 0
            
            return math.floor((-1 + math.sqrt(1 + 4 * instances)) / 2)
        
        
        def maxRows(type1, type2):
            first = numRowsIfFirst(type1) * 2
            second = numRowsIfSecond(type2) * 2
            
            
            print(first, second)
            if second >= first:
                return first
            else:
                # first > second
                return second + 1
                
        return max(maxRows(red, blue), maxRows(blue, red))
                
