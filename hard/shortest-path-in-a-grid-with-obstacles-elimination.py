from queue import Queue
class Node: 
    def __init__(self, i, j, visited_by_k, dist):
        self.i = i
        self.j = j
        self.visited_by_k = visited_by_k
        self.dist = dist
    
    def __str__(self):
        return (f"{self.i}  {self.j}  {self.visited_by_k}   {self.dist} ")
MAX_INT = 12312312312
class Solution:
    nodes = {} # take tuple as key
    _min = MAX_INT
    pq = Queue()
    
    def shortestPath(self, grid, k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1: return 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.visited = []
        for i in range(self.m):
            a = []
            for j in range(self.n):
                a.append(set({}))
            self.visited.append(a)
        
        self.pq.put(Node(self.m-1, self.n-1, k, 0))

        while not self.pq.empty():
            top = self.pq.get()
            i = top.i
            j = top.j
            k = top.visited_by_k
            dist = top.dist

            if (i, j) == (0, 0):
                self._min = dist if dist < self._min else self._min
                break
            
            tup_arr = self.tuple_pairs(i,j)
            for tup in tup_arr: 
                if k not in self.visited[tup[0]][tup[1]]:
                    self.visited[tup[0]][tup[1]].add(k)
                    if self.grid[tup[0]][tup[1]] == 1:
                        if k > 0:
                            self.pq.put(Node(tup[0], tup[1], k-1, dist+1))
                    else:
                        self.pq.put(Node(tup[0], tup[1], k, dist +1))
                        
        return self._min if self._min != MAX_INT else -1

    def tuple_pairs(self, i, j):
        i_p = []
        j_p = []
        if i +1 < self.m:
            i_p.append(i+1)
        if i -1 >= 0:
            i_p.append(i-1)
        if j +1 < self.n:
            j_p.append(j +1)
        if j-1 >= 0:
            j_p.append(j -1)
            
        pairs = [] 
        for _i in i_p:
            pairs.append( (_i, j))
        for _j in j_p:
            pairs.append( (i, _j))

        return pairs
