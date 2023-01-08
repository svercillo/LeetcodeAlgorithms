class Solution:
    def insert(self, intervals, newInterval):

        to_remove = []
        not_set = True

        if len(intervals) == 0:
            return [newInterval]
        if newInterval[0] < intervals[0][0]:
            not_set = False
            print("SDFSDFSDF")
            starting = 0

        for i, interval in enumerate(intervals):

            if not_set:
                if newInterval[0] <= interval[1]:
                    starting = i
                    not_set = False
                    if newInterval[1] >= interval[0]:
                        to_remove.append(i)

            else:
                if newInterval[1] >= interval[0]:
                    to_remove.append(i)

        if not_set:
            starting = len(intervals)

        if len(to_remove) == 0:
            intervals.insert(starting, newInterval)

        else:
            _max = max(newInterval[1], intervals[to_remove[-1]][1])
            _min = min(newInterval[0], intervals[to_remove[0]][0])
            for i in to_remove[::-1]:
                intervals.pop(i)

            intervals.insert(i, [_min, _max])

        return intervals
