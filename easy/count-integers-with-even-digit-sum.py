class Solution:
    def countEven(self, num: int) -> int:
        
        count = 0
        for n in range(1, num+1):
            
            digitsum = 0
            for c in str(n):
                digitsum += int(c)
                
            
            
            print(digitsum, n)
            if digitsum % 2 == 0:
                count += 1
                
        
        return count
                
                
