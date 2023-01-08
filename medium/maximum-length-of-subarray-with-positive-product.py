import math


class Solution:
    def getMaxLen(self, nums) -> int:

        stopinds = []
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                stopinds.append(i)

        stopinds.append(n)

        # print(stopinds)

        def process_subarray(start, stop):

            # print(start, stop, nums[start:stop])
            nstart, nend, ncount = -1, -1, 0
            for i in range(start, stop):

                if nums[i] < 0:
                    ncount += 1
                    if nstart == -1:
                        nstart = i
                    nend = i

            if ncount % 2 == 0:
                return stop - start

            else:
                if nstart == nend:
                    return max(stop - 1 - nstart, nend - start)

                return max(stop - 1 - nstart, nend - start)

        _max = 0
        for i in range(0, len(stopinds)):
            if i == 0:
                res = process_subarray(0, stopinds[i])
            else:
                res = process_subarray(stopinds[i - 1] + 1, stopinds[i])

            if res > 0:
                _max = max(_max, res)

        return _max
