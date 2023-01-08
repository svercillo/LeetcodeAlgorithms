import heapq



def calc_dist(x1, y1, x2, y2):
    return ((x1 - x2) **2 + (y1 - y2) **2) ** 0.5


class Solution:
            
    def minKnightMoves(self, x: int, y: int) -> int:
        
        
        dirs = [[1, 1], [1, -1], [-1,-1], [-1,1]]
        vecs = [[2, 1], [1,2]]
        
        visited = set()
        q = [(0,0)]
        
        steps = 1
        while q:
            newq = [] 
            for i, j in q:
                if (i,j) in visited:
                    continue
                
                visited.add((i,j))
                
                for d in dirs: 
                    for v in vecs: 
                        ti = i + d[0] * v[0]
                        tj = j + d[1] * v[1]
                        
                        if (ti, tj) == (x, y): 
                            return steps
                        newq.append((ti, tj))
            steps +=1 
            q = newq        
                    
                        
                
                
        
                        
                        
                        
                        
        
                
        
        
        
        
            
