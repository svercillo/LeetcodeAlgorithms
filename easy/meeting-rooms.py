class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda k : k[0])

        
        end = 0
        for inval in intervals:
            if inval[0] >= end:
                end = inval[1]
            else:
                return False
        
        return True
                
            
            
            
