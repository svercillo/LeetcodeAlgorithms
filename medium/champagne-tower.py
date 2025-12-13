class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if not poured:
            return 0

        q = [poured]
        for depth in range(query_row):
            nq = []
            for i, fill in enumerate(q):
                if i == 0:
                    tofill = max(0, fill -1) / 2
                else:
                    tofill = (max(0, fill  -1) + max(0, q[i-1] - 1)) / 2

                nq.append(tofill)
                
            tofill = max(0, q[-1] -1) / 2
            nq.append(tofill)
            q = nq
        return min(q[query_glass], 1)            
