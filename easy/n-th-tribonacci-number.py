class Solution:
    def tribonacci(self, n: int) -> int:
        visited = {}
        def tribonacci(num):
            if num in visited: 
                return visited[num]
            
            if num == 0:
                res = 0
            elif num == 1:
                res =  1
            elif num == 2:
                res =  1
            else:
                res = tribonacci(num-1) + tribonacci(num-2) + tribonacci(num-3)
            visited[num] = res

            return res

        return tribonacci(n)
