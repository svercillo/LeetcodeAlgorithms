from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n 
        q = deque()
        dp[0] = nums[0]
        
        for i, e in enumerate(nums):
            if i ==0:
                q.append(i)
                continue


            while q[0] < i - k:
                q.popleft()

            dp[i] = e + dp[q[0]]
 
            while len(q) and dp[i] >= dp[q[-1]]:
                q.pop()

            
            q.append(i) # smallest in q
        return dp[-1]

