import heapq
import math
class Solution:  
    class Node: 
        def __init__(self, val, dist, in_q=False):
            self.val = val
            self.dist = dist
            self.visited = False
            self.in_q = in_q
            
        def __lt__(self, that):
            return self.dist > that.dist # we want a reversed heap
        
        def __repr__(self):
            return f"<{self.val}, {self.dist}, {int(self.visited)}>"
            
    def maxProbability(self, n: int, edges, succProb, start: int, end: int) -> float:
        if start == end: return 1
        conns = {}
        for i in range(len(edges)):
            e = edges[i]
            p = succProb[i]
            
            if e[0] not in conns: 
                conns[e[0]] = {e[1] : p}
            else:
                conns[e[0]][e[1]] = p 
            
            if e[1] not in conns: 
                conns[e[1]] = {e[0] : p}
            else:
                conns[e[1]][e[0]] = p 
        
        if start not in conns: return 0 # no paths out
        nodes = { n : self.Node(n, 0) for n in conns}
            
        
        nodes[start].dist = 1 # 100 % prob of staying home
        nodes[start].in_q = True
        
        queue = [nodes[start]]

        while len(queue) > 0:
            top = heapq.heappop(queue)
            if top.visited:
                continue

            index = top.val
            for neighbor_key in conns[index]: 
                
                neighbor = nodes[neighbor_key]
                if neighbor.visited:
                    continue
                
                new_prob = top.dist *  conns[top.val][neighbor.val]
                if new_prob > neighbor.dist:
                    neighbor.dist = new_prob
                    heapq.heappush(queue, neighbor)
                    
                 
            top.visited = True
            
            
        return nodes[end].dist if end in nodes else 0
