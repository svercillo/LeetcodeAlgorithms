import heapq

class Solution:
    class Node:
        def __init__(self, i, j, dist):
            self.i = i
            self.j = j
            self.dist = dist

        def __lt__(self, other):
            return self.dist < other.dist

        def __repr__(self):
            return f"Node<{self.i}, {self.j}, {self.dist} >"

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                dirs.append((i,j))
        

        if grid[0][0] != 0: # can't start
            return -1

        
        q = [self.Node(0, 0, 1)]

        visited = set()

        while len(q):
            node = heapq.heappop(q)
            if (node.i, node.j) in visited:
                continue
            visited.add((node.i, node.j))


            if node.i == n-1 and node.j == n-1:
                return node.dist 

            for down, right in dirs:
                ti = node.i + down
                tj = node.j + right

                if 0 <= ti < n and 0 <= tj < n and grid[ti][tj] == 0:
                    heapq.heappush(q, self.Node(ti,tj,node.dist +1))

        return -1 # impossible
            
