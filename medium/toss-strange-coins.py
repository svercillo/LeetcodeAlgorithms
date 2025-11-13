class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        n = len(prob)
        
        @cache
        def solve(ind, used):
            if ind == n:
                return 1 if used == target else 0
            
            if used < target:
                return (
                    prob[ind] * solve(ind + 1, used + 1) + 
                    (1 - prob[ind]) * solve(ind + 1, used)
                )
            
            return (1 - prob[ind]) * solve(ind + 1, used)

            

    
        
        return solve(0, 0)
