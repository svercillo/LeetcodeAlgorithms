class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [ 0 ] *( len(s) +1 )

        dp_arr = []
        for i in range(len(s) +1):
            dp_arr.append([])
            
        
        hashset = set(wordDict) 
        
        
        dp[0] =1
        
        for i in range(0, len(s)):
            for j in range(i, -1, -1):
                
                sub = s[j : i+1]
                stop = False
                if dp[j]:
                    for key in hashset:
                        if key == sub:
                            stop = True
                            dp[i+1] =1

                            if j ==0:
                                dp_arr[i+1].append(key)
                                
                            else:
                                for string in dp_arr[j]:    
                                    dp_arr[i+1].append(string + " " + key)
        
        return dp_arr[len(dp)-1]
