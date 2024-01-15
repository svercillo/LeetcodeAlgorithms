class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        _, lend = intervals[0]
        num_removed = 0
        for start, end in intervals[1:]:
            if start < lend:
                # print(start, end)
                num_removed += 1
                lend = min(end, lend)
            else:
                # no overlap
                lend = end
        return num_removed
