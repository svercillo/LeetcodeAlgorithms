class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # merge intervals? 

        meetings.sort(key = lambda k:k[0]) 

        intervals = []
        previous_start, previous_end =  meetings[0]

        for start, end in meetings:
            if start > previous_end:
                intervals.append(
                    (previous_start, previous_end)
                )

                previous_start = start
                previous_end = end
                
            elif end > previous_end:
                previous_end = end                
                    
        intervals.append(
            (previous_start, previous_end)
        )        

        if len(intervals) == 0:
            return n
        
        res = 0
        for i in range(len(intervals)-1):
            int1 = intervals[i]
            int2 = intervals[i+1]

            res += int2[0] - int1[1] -1 

        res += intervals[0][0] -1
        res += days - intervals[-1][1]

        return res
