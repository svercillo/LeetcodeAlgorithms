class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        if n ==2:
            return k*k
        if n ==1:
            return k
    
                
        res = 0
        
        states = [k, k * (k-1)]
        for i in range(2, n):

            
            old_state0 = states[0]
            states[0] = states[1] * 1
            
        
            states[1] = old_state0 * (k-1) + states[1] * (k-1)
            
    
        return sum(states)
    
