class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        count = 0
        def dfs(n):
            nonlocal count
            
            if n == 0: 
                return
            
            count += 1
            if n % 2 == 0:
                dfs(n /2)
            else:
                dfs(n -1)
        dfs(num)
        return count