class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n, m = len(heights), len(heights[0])

        dirs = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]

        @cache
        def can_flow_to_ocean(i, j, is_pacific):
            nonlocal n, m

            if i < 0 or j < 0:
                return is_pacific 

            if i >= n or j >= m:
                return not is_pacific

            print(i, j)
            for down, right in dirs:
                ti = i + down
                tj = j + right

                if (ti, tj) in path:
                    continue

                if 0 <= ti < n and 0 <= tj < m:
                    if heights[ti][tj] > heights[i][j]:
                        continue

                path.add((ti, tj))
                
                if can_flow_to_ocean(ti, tj, is_pacific):
                    path.remove((ti, tj))
                    return True
                
                else: 
                    path.remove((ti, tj))



            return False
                
                

        res = []
        for i in range(n): 
            for j in range(m):
                path = set([(i, j)])
                flow_p = can_flow_to_ocean(i, j, True)
                path = set([(i, j)])
                flow_a = can_flow_to_ocean(i, j, False)


                if flow_p and flow_a:
                    res.append([i, j])
        
        return res
