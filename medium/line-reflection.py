class Solution:

    def isReflected(self, points: List[List[int]]) -> bool:


        l, r = math.inf, -math.inf
        for j, i in points:
            l = min(j, l)
            r = max(j, r)
        
        linex = (l + r) / 2

        prevpoints = set([tuple(e) for e in points])
        npoints = set()
        for j, i in points:
            
            diff = abs(j - linex)
            if j <= linex:
                npoints.add((linex + diff, i))
            else:
                npoints.add((linex  - diff, i))
        return npoints == prevpoints




    
