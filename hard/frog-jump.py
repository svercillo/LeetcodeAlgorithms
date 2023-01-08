class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        dp = {} # stone_ind : {prevjump: possible} 
        
        
        possible_jump_diffs = [-1, 0, 1]
        
        def dfs(i, prev_jump):
            
            if (i, prev_jump) in dp: 
                return dp[(i, prev_jump)]
        
            if i == len(stones) -1: 
                dp[(i, prev_jump)] = True
                return True
            
            j = i +1
            res = []
            while j < len(stones) and stones[j] - stones[i] <= prev_jump +1:
                
                for p in possible_jump_diffs:
                    jump_dist = prev_jump + p 
                    if stones[i] + jump_dist == stones[j]:
                        res.append(dfs(j, jump_dist))
                
                j += 1
                
            for r in res: 
                if r:
                    dp[(i, prev_jump)] = True
                    return True
                    
                
            dp[(i, prev_jump)] = False
            return False
            
            
        
                
        return dfs(0, 0)
