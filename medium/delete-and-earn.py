class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = {} 

        for e in nums:
            if e not in freq: 
                freq[e] = 0
            freq[e] += 1

        dp = []
        arr = []
        for k in freq:
            freq[k] = freq[k] * k
            arr.append(k)
            dp.append([-1, -1])
        
        arr.sort()

        dp[0][0] = freq[arr[0]] # take
        dp[0][1] = 0 # don't take

        for i in range(1, len(arr)):
            k = arr[i]
            # take
            value = freq[k]
            prev_k = arr[i-1]
            if prev_k != k -1:
                value += max(dp[i-1]) # max of take or don't take k-1
            else:
                value += dp[i-1][1] # don't take last one

            dp[i][0] = value

            # don't take
            dp[i][1] = max(dp[i-1]) # max of take or don't take k-1

            x = 1 

        return max(dp[len(arr)-1])
