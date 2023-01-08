import heapq

class Node:
    def __init__(self, effort, i, j):
        self.effort = effort
        self.i = i
        self.j = j
        
    def __lt__(self, other):
        
        if self.effort != other.effort:
            return self.effort < other.effort
        else: 
            return (self.i + self.j) > (other.i + other.j)
        
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    
        n = len(heights)
        m = len(heights[0])
        
        q = [Node(0,0,0)] # effort, i, j
        
        paths = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        
        result = 0
        visited = set()
        while len(q):
            top = heapq.heappop(q)
            
            result = max(result, top.effort)
            if top.i == n-1 and top.j == m-1:
                break
            
            visited.add((top.i, top.j))
            
            for p in paths:
                new_i = top.i + p[0]
                new_j = top.j + p[1]
                
                if 0 <= new_i < n and 0 <= new_j <m and (new_i, new_j) not in visited:
                    
                    effort = abs(heights[new_i][new_j] - heights[top.i][top.j])
                    heapq.heappush(q, Node(effort, new_i, new_j))
        
                    
                
        return result
