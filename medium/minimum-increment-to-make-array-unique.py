import heapq
from collections import defaultdict

class Solution:
    def minIncrementForUnique(self, nums) -> int:

        freqs = defaultdict(lambda : 0)

        for c in nums:
            if c not in freqs:
                freqs[c] = 0
            freqs[c] += 1

        keys = [k for k in freqs]
        heapq.heapify(keys)

        count = 0
        while len(keys):
            # print(keys)
            value = heapq.heappop(keys)


            if freqs[value] == 1:
                continue

            assert value in freqs

            
            if not len(keys) or keys[0] != value + 1:
                heapq.heappush(keys, value + 1)

            
            count += freqs[value] - 1
            freqs[value + 1]  += freqs[value] - 1

        # print(keys)
        return count
