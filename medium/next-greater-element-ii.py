from collections import deque

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = deque()

        dp = [-1] * n
        for i in range(n*2):
            j = i % n 

            while len(stack) and nums[j] > stack[-1][1]:
                ind, _ = stack.pop()
                dp[ind] = nums[j]
            
            stack.append((j, nums[j]))


        return dp
