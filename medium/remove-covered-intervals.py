class Solution:
    def removeCoveredIntervals(self, intervals) -> int:
        
        intervals.sort(key = lambda ele : (ele[0], -ele[1]))
        i =0 
        while i < len(intervals)-1 :
            if intervals[i] == intervals[i+1]:
                intervals.pop(i)
            i +=1 
        
        n = len(intervals)
        intervals2 = sorted(intervals, key = lambda ele : (ele[1], -ele[0]))
        forward = {}
        backward = {} 
        
#         for i,val in enumerate(intervals): 
#             forward[tuple(val)] = i
        
        print(intervals)
        print( intervals2)
        for i, val in enumerate(intervals2): 
            backward[tuple(val)] = i
        
        
        
        removed_cnt = 0
        i = 0
        while i < len(intervals):
            
            
            invalid = False
            f = i
            b = backward[tuple(intervals[i])]

            # print(intervals[i])
            f_set = set({})
            b_set = set({})
            f -=1
            b +=1 
            while f >=0 or b < n:
                
                if f >= 0:
                    if tuple(intervals[f]) in b_set:
                        invalid = True
                        break
                    f_set.add(tuple(intervals[f]))
                    
                if b < n: 
                    if tuple(intervals2[b]) in f_set:
                        invalid = True
                        break 
                    b_set.add(tuple(intervals2[b]))

                if f >=0 and b < n:
                    if tuple(intervals[f]) == tuple(intervals2[b]):
                        invalid = True
                        break 
                


                    
                f -= 1 
                b +=1
            
            
            if invalid:
                print(intervals[i])
                removed_cnt += 1
                
            i +=1 
                
        
        return n - removed_cnt
                    
