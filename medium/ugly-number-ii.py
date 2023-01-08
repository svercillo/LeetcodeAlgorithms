class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        q = [1]
        visited = set()        
        while n:

            num = heapq.heappop(q)

            for multiplier in [2, 3, 5]:
                new_value = num * multiplier

                if new_value not in visited: 
                    heapq.heappush(q, new_value)
                visited.add(new_value)

            n -= 1        


        return num
            
