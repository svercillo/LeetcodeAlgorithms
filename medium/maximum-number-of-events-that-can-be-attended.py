class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:


        n = len(events)


        start_map = {}

        first_day = math.inf
        last_day = -math.inf

        for i, e in enumerate(events):
            if e[0] not in start_map:
                start_map[e[0]] = []

            first_day = min(first_day, e[0])
            last_day = max(last_day, e[1])

            start_map[e[0]].append(i)

        total = 0
        q = []
        for d in range(first_day, last_day+1):
            if d in start_map:
                for ind in start_map[d]: 
                    heapq.heappush(q, events[ind][1])

            while len(q) and q[0] < d:
                heapq.heappop(q )

            if len(q): 
                end = heapq.heappop(q)
                total += 1
        return total

            
