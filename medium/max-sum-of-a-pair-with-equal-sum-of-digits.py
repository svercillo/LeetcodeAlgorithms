import heapq
from collections import OrderedDict


class Solution:
    def maximumSum(self, nums) -> int:
        class Num:
            def __init__(self, val):
                self.val = val

            def __lt__(self, other):
                return self.val > other.val

            def __repr__(self):
                return str(self.val)

        sum_digs = {}

        for n in nums:
            _sum = 0
            for c in str(n):
                _sum += int(c)

            if _sum not in sum_digs:
                sum_digs[_sum] = []

            heapq.heappush(sum_digs[_sum], Num(int(n)))

        print(sum_digs)

        _max = -1

        for n in sum_digs:
            if len(sum_digs[n]) >= 2:
                total_sum = (
                    heapq.heappop(sum_digs[n]).val + heapq.heappop(sum_digs[n]).val
                )
                _max = max(_max, total_sum)

        return _max
