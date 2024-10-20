class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        
        dp = {}
        
        for e in nums:
            mod = e % space
            if mod not in dp: 
                dp[mod] = []

            dp[mod].append(e)


        smallestLen = max([len(dp[mod]) for mod in dp ])


        res = set()
        for mod in dp:
            if len(dp[mod]) == smallestLen:
                res = res.union(dp[mod])
        
        return min(res)
                
