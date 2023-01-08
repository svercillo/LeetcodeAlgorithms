class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        res = 0
        for o in operations:
            if o.find("++") != -1:
                res +=1
            else: 
                res -= 1 
                
        return res 
                

            
