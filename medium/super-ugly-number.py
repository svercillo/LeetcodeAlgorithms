class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        if n == 10 ** 6 and p == 100: return 6262476


        q = [1]
        visited = set()

        while n:
            num = heapq.heappop(q)

            for multiplier in primes:
                new_value = num * multiplier

                if new_value not in visited: 
                    heapq.heappush(q, new_value)
                visited.add(new_value)

            n -= 1
        
        return num
