from pprint import pprint

class Solution:
    def pacificAtlantic(self, heights):
        n, m = len(heights), len(heights[0])


        oceans = []
        for i in range(n):
            row = []
            for j in range(m): 
                row.append(0)
            oceans.append(row)
        
        
        startingP = [ (0,i) for i in range(m)] + [ (i,0) for i in range(n)]
        startingA = [ (n-1,i) for i in range(m)] + [ (i,m-1) for i in range(n)]
        


        dirs = [ 
            [0, 1],
            [0, -1], 
            [-1, 0 ],
            [1, 0]
        ]

        for (pacific, context) in enumerate([ startingA, startingP]):
            queue = context
        
            print(queue)
            visited = set()
            while len(queue): 
                nqueue = []
                for i, j in queue: 

                    if pacific:
                        oceans[i][j] |= 1
                    else:
                        oceans[i][j] |= 2
                
                    if (i, j) in visited:
                        continue
                    visited.add((i, j))
                    
                    for down, right in dirs:
                        ti = i + down
                        tj = j + right


                        # if out of bounds
                        if not (0<= ti < n and 0<= tj < m):
                            continue
                        
                        # if cannot travel
                        if heights[ti][tj] < heights[i][j]:
                            continue
                        
                        nqueue.append((ti, tj))
                queue = nqueue
                # break
            
        res = []
        for i in range(n):
            for j in range(m):
                if oceans[i][j] == 3:
                    res.append((i, j))


        pprint(oceans)
        
        return res
        




                    











            









    



        

res = Solution().pacificAtlantic(
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]  
)

 
print(res)
