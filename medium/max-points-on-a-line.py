import math
import itertools
class Solution:
    def maxPoints(self, points) -> int:  
        n = len(points)
        pairs = [p for p in itertools.combinations(points, 2)]

        
        lines = {}
        for p1, p2 in pairs:
            y_diff = p2[1] - p1[1]
            x_diff = p2[0] - p1[0]
            
            if p1[0] > p2[0]:
                t = p1
                p1 = p2
                p2 = t

            if x_diff == 0:
                m = math.inf
                b = p2[0]
            elif y_diff == 0:
                m = p2[1]
                b = math.inf
            else:
                m = y_diff / x_diff
                b = p2[1] - m * p2[0]

            if (m, b) not in lines:
                lines[(m,b)] = set()
                    
            lines[(m,b)].add(tuple(p1))
            lines[(m,b)].add(tuple(p2))


        _max = 1
        for m_b in lines:
            _max = max(len(lines[m_b]), _max) 

        return _max
