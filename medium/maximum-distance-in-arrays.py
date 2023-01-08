class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        
        mxi, mni = -1, -1
        smxi, smni = -1, -1
        
        mx, mn = -math.inf, math.inf
        smx, smn = -math.inf, math.inf
        for i in range(m):
            
            if arrays[i][-1] >= mx:
                smxi = mxi
                smx = mx
                
                mxi = i
                mx = arrays[i][-1]
            elif arrays[i][-1] >= smx:
                smxi = i
                smx = arrays[i][-1]
            
            
            if arrays[i][0] <= mn:
                smni = mni
                smn = mn
                
                mni = i
                mn = arrays[i][0]
            elif arrays[i][0] <= smn:
                smni = i
                smn = arrays[i][0]
        
        if mxi == mni:
            return max(
                [
                    arrays[mxi][-1]-arrays[smni][0], 
                    arrays[smxi][-1]-arrays[mni][0]
                ]
            )
            
        else:
            return arrays[mxi][-1] - arrays[mni][0]
