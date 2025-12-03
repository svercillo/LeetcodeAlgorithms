class Solution:
    def maxFreeTime(self, eventtime: int, startTime: List[int], endTime: List[int]) -> int:
        events = list(zip(startTime, endTime))
        n = len(events) 
        
        gaps = [events[0][0]]
        for i in range(n):
            rbarrier = events[i+1][0] if i < n-1 else eventtime
            rgap = rbarrier - events[i][1]
            gaps.append(rgap)
        # # print(gaps)


        prun = gaps[0]
        srun = gaps[-1]
        prefix = [None] * len(gaps)
        suffix = [None] * len(gaps)

        for i in range(len(gaps)): 
            prun = max(prun, gaps[i])
            prefix[i] = prun

            sind = len(gaps) -1 - i
            srun = max(srun, gaps[sind])
            suffix[sind] = srun
        # print(prefix, suffix)

        res = 0
        for i in range(n ): 
            start, end = events[i]
            duration = end - start

            lbarrier = events[i-1][1] if i > 0 else 0 
            rbarrier = events[i+1][0] if i < n-1 else eventtime

            # print((start, end), i, "duration " , duration)
            if (
                (i < len(suffix) - 2  and suffix[i+ 2] >= duration) or 
                (i > 0 and prefix[i-1] >= duration)
            ):
                # # print("SDFSDF", (rbarrier,  lbarrier))
                res = max(res, rbarrier - lbarrier)
            else: 
                res = max(res, rbarrier - lbarrier - duration)
        return res

            
            
