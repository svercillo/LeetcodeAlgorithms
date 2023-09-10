class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSym(num):
            string = str(num)
            if len(string) % 2 == 1:
                return False
            
            
            sum1 = 0
            for i in range(len(string) //2): 
                sum1 += int(string[i])
                
            sum2 = 0
            for i in range(len(string)//2, len(string)):
                sum2 += int(string[i])
                
            return sum1 == sum2
                
            
        count = 0        
        for num in range(low, high +1):
            count += 1 if isSym(num) else 0
            
        return count
            
    
