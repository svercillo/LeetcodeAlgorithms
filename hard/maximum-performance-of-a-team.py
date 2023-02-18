class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        zipped = zip(speed, efficiency)
        zipped = sorted(zipped, key = lambda arr : (-arr[1], arr[0])) # sort by efficiency

        speed_sum = {}
        speeds = []
        presum_speed = 0
        for speed, efficiency in zipped:
            if len(speeds) == k:
                slowest = heapq.heappop(speeds)
                presum_speed -= slowest
            presum_speed += speed
            heapq.heappush(speeds, speed)
            speed_sum[efficiency] = presum_speed

        possible = []

        for eff in speed_sum:
            possible.append(eff * speed_sum[eff])

        
        largest = 0 
        for poss in possible:
            largest = max(largest, poss)

        return largest % (10 ** 9 + 7) 
