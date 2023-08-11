class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0] )
        thieves = []
        _map = []
        for i in range(n):
            row = [] 
            for j in range(m):
                if grid[i][j] == 1:
                    thieves.append((i,j))
                row.append(-1)

            _map.append(row)


        dirs = [
            [0,1],
            [1, 0],
            [0,-1],
            [-1, 0]
        ]
        visited = set()
        man_dist = 0
        q = thieves
        while len(q):
            new_q = [] 
            for i, j in q:

                if (i, j) in visited:
                    continue

                visited.add((i,j))

                _map[i][j] = man_dist
                
                for down, right in dirs:
                    ti = i + down
                    tj = j + right

                    if (0<= ti < n) and (0<=tj < m):
                        new_q.append((ti, tj))
            q = new_q
            man_dist += 1
        
        class Node:
            def __init__(self, i, j, safety): 
                self.i = i
                self.j = j
                self.safety = safety

            def __lt__(self, other): 
                return self.safety > other.safety


        # print(_map)
        visited = set()
        q = [Node(0, 0, _map[0][0])]
        while q:
            
            top = heapq.heappop(q)
            
            
            i = top.i
            j = top.j
            safety = top.safety

            # print("node", i, j, safety )
            if (i, j) in visited:
                continue
            elif (i, j) == (n-1, m-1):
                return top.safety
            
            visited.add((i, j))

            for down, right in dirs:
                ti = i + down
                tj = j + right

                if (0 <= ti < n) and (0 <= tj < m):
                    new_node = Node(ti, tj, min(safety, _map[ti][tj]))
                    heapq.heappush(q, new_node)


        return -1

