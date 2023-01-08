class Solution:
    def totalMoney(self, n: int) -> int:
        
        last_day = 0
        last_monday =0 
        _sum = 0
        last = 0
        for i in range(0, n):
            if i % 7 ==0:
                _sum += last_monday + 1 
                last = last_monday + 1
                last_monday += 1
            else:
                _sum += last +1
                last += 1
                
        
            print(_sum)
        return _sum
                
                
                
                
            
