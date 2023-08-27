class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        
        mid_target = target // 2
        
        print(mid_target)



        # 3 cases
        if mid_target >= n:    
            return (n+ 1) * n //2


        line1 = (mid_target +1) * mid_target // 2
        delta = n -mid_target 
        topline2 = target + delta - 1
        bottomline2 = target - 1
        line2 = (topline2 * (topline2 +1) // 2)  - (((bottomline2 + 1) * bottomline2) // 2)
        

    
        ''' 
        1. 2* sum(mid_target) - sum (target) + (target -mid_target + target) * (target -mid_target + target

        '''


                
        return line1 + line2 
        
