from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap):
        n, m = len(heightMap), len(heightMap[0])
        vis = [[False]*m for _ in range(n)]
        heap = []

        # push all border cells
        for i in range(n):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][m-1], i, m-1))
            vis[i][0] = vis[i][m-1] = True

        for j in range(m):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[n-1][j], n-1, j))
            vis[0][j] = vis[n-1][j] = True

        res = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while len(heap):
            h, i, j = heappop(heap)

            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if not (0 <= ni < n and 0 <= nj < m): 
                    continue
                if vis[ni][nj]: 
                    continue

                vis[ni][nj] = True

                # if neighbor lower, water trapped = h - height
                nh = heightMap[ni][nj]
                if nh < h:
                    res += h - nh

                # push boundary height = max(nh, h)
                heappush(heap, (max(nh, h), ni, nj))

        return res
