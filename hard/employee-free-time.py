class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        
        intervals = [] 
        for emp in schedule:
            for k in emp:
                intervals.append(k)
            
        intervals.sort(key = lambda k : k.start)
        
        merged = []
        intv = intervals[0]        
        start = intv.start
        end = intv.end
        
        first = True
        
        
        for intv in intervals:
            if first:
                first = not first
                continue
                    
            tstart, tend = intv.start, intv.end
            
            if tstart > end:
                tintv = Interval(start, end)
                merged.append(tintv)
                start, end  = tstart, tend
            else:
                start = min(start, tstart)
                end = max(end, tend)
        
        merged.append(Interval(start, end))
        print([(m.start, m.end) for m in merged])
        

        res = []
        for i in range(len(merged) -1):
            

            res.append(Interval(merged[i].end, merged[i+1].start))

            
        return res
            
            
        
        
        
        
