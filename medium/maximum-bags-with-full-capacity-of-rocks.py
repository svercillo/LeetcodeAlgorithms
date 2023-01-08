from collections import deque

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        n = len(capacity)
    
        space = []
        for i in range(n):
            space.append(capacity[i] - rocks[i])

        space.sort()

        space = deque(space)

        count = 0
        while additionalRocks > 0 and len(space):
            top = space.popleft()
            if additionalRocks >= top:
                count += 1
                additionalRocks -= top

            print(top)

        
        return count
