class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        start = floor(area ** 0.5)
        
        while True:
            
            if area % start == 0:
                return [area // start,  start]
            
            
            
            start -=1
        
