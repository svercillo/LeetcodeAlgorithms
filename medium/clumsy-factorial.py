class Solution:
    def clumsy(self, n: int) -> int:
        
        total = 0
        count = 0
        temp_not_set = False
        temp = 1
        positive = True
        for ind in range(n, 0, -1):
            
            if count % 4 == 3:
                total += ind
            elif count % 4 == 0:
                temp_not_set = True
                temp = ind
            elif count % 4 == 1:
                temp *= ind
            elif count % 4 == 2:
                temp //= ind
                
                if positive:
                
                    total += temp
                else:
                    total -= temp 

                positive = False
                temp_not_set = False
            
            count += 1

        if temp_not_set:
            if positive:
                total += temp
            else:
                total -= temp 


        
        
        return total
