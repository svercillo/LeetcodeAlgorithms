class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        freq = {}
        for e in arr:
            if e not in freq: 
                freq[e] = 0
            freq[e] += 1

        if difference == 0:
            return max([freq[k] for k in freq])

        dp = {}
        for e in arr:
            if e - difference in dp:
                dp[e] = dp[e - difference] + 1
            else:
                dp[e] = 1
            
        _max = 0
        for e in dp:
            _max = max(_max, dp[e])


        print(dp)
        return _max 


        
            

