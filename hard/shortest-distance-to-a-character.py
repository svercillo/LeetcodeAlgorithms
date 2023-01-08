class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        directions = [
            [1, 0], [0,1], [-1,0], [0, -1]
        ]


        n, m = len(grid), len(grid[0])

        visited = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(set())
            visited.append(row)

        blocks = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    blocks[(i,j)] = 1

        steps = 0
        q = [[0,0, k]]

        while len(q):
            new_q = []
            for i, j, k in q: 
                if k in visited[i][j]:
                    continue
                visited[i][j].add(k)
                
                if (i,j) == (n-1, m-1):
                    return steps # first to reach destination

                for down, right in directions:
                    ti = i + down
                    tj = j + right

                    if 0 <= ti < n and 0 <= tj < m:
                        if grid[ti][tj] == 1:
                            if k > 0:                                
                                new_q.append((
                                    ti, 
                                    tj, 
                                    k - 1
                                ))
                        else:
                            new_q.append((ti, tj, k))
            q = new_q
            steps += 1
        return -1
