import math
from functools import lru_cache
class Solution:
    def minJumps(self, forbidden, a, b, x):

        forbidden = set(forbidden)
        visited = set()

        def num_moves(pos, current_moves):
            nonlocal a, b, x

            if pos > 12 * x * b: 
                return -1

            if pos == x:
                visited.add(pos)
                return current_moves

            visited.add(pos)

            min_moves = math.inf
            if pos + a not in forbidden and pos + a and pos + a not in visited:
                min_moves = num_moves(pos + a, current_moves+1)
            

            if pos - b not in forbidden and pos - b > 0 and pos -b  and  pos + b not in visited:
                min_moves = min(
                    min_moves, 
                    num_moves(pos - b, current_moves+1)
                )

            
            return min_moves 


        return num_moves(0, 0)

res = Solution().minJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11)
res = Solution().minJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9)
print(res)



        
        
