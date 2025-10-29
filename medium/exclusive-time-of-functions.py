class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        usages = [0] * (n + 1)

        events = []

        for log in logs:
            fid, atype, ts = log.split(":")
            fid = int(fid)
            ts = int(ts)

            if atype == "end": 
                ts += 1

            events.append((fid, atype, ts))


        events.sort(key = lambda k : k[2])
        events = deque(events)

        callStack = [n]
        lastTs = 0
        lastFid = n
        lastA = None
        for fid, atype, ts in events:
            previous = callStack[-1]

            if atype == "start":
                usages[previous] += ts - lastTs

                callStack.append(fid)
            else:
                usages[previous] += ts - lastTs
            
                callStack.pop()
            
            lastTs = ts
            lastFid = fid
            lastA = atype

        return usages[:-1]



