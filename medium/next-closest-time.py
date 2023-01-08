import math

class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        
        numbers = set()
        for c in time: 
            if c != ":":
                numbers.add(int(c))
                
        hrs = int(time[:2])
        mins = int(time[3:])
        
        curr_min_cnt = hrs * 60 + mins
                
        H1 = set([int(time[0])])
        H2 = set([int(time[1])])
        M1 = set([int(time[3])])
        M2 = set([int(time[4])])
        
        
        for n in numbers:
            H2.add(n)
            M2.add(n)
            
            if n <= 5:
                M1.add(n)
                
            if n <= 2: 
                H1.add(n)
                
                
        
        min_diff = math.inf 
        min_hrs = math.inf
        min_mins = math.inf
        
        
        for h1 in H1:
            for h2 in H2: 
                for m1 in M1:
                    for m2 in M2: 
                        if h1 == 2 and h2 >= 4: 
                            continue
                            
                        
                        n_hrs = int(str(h1) + str(h2))
                        n_mins = int(str(m1) + str(m2))
                        
                        
                        next_day = False 
                        if n_hrs < hrs or n_hrs == hrs and n_mins < mins:
                            next_day = True
                            n_hrs += 24
                        
                        min_count = n_hrs * 60 + n_mins
                        diff = min_count - curr_min_cnt
                        if diff == 0:
                            diff = 3600
                        print(h1, h2, m1, m2)
                        print("diff", diff)
                        
                        if diff < min_diff:
                            min_diff = diff
                        
                            min_hrs = n_hrs if not next_day else n_hrs - 24 
                            min_mins = n_mins
        
                            
        return f"{min_hrs if len(str(min_hrs)) ==2 else f'0{min_hrs}'}:{min_mins if len(str(min_mins)) == 2 else f'0{min_mins}'}"
                        
                        
                        
                            
