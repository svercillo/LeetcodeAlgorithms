class Solution:
    def countCoveredBuildings(self, n: int, coords: List[List[int]]) -> int:
        '''
        for each column store min max i seen 
        for each row store min max j seen
        '''

        minicols = defaultdict(lambda : math.inf)
        maxicols = defaultdict(lambda : -math.inf)

        minjrows = defaultdict(lambda : math.inf)
        maxjrows = defaultdict(lambda : -math.inf)

        for i, j in coords:
            minicols[j] = min(minicols[j], i)
            maxicols[j] = max(maxicols[j], i)

            minjrows[i] = min(minjrows[i], j)
            maxjrows[i] = max(maxjrows[i], j)



        res = 0
        for i, j in coords: 
            if minicols[j] < i < maxicols[j] and minjrows[i] < j < maxjrows[i]:
                res += 1
            
            
        return res
