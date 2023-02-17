from collections import deque
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # monotonic stack

        n = len(heights)
        res = [0] * n 
        stack = deque() # monotonically decreasing stack
        for i, h in enumerate(heights):
            

            while len(stack) > 0 and h > stack[-1][0]:
                _, j = stack.pop()
                res[j] += 1
                
            stack.append((h, i))
            if len(stack) >= 2:
                ind = stack[-2][1]
                res[ind] += 1
        
        return res
