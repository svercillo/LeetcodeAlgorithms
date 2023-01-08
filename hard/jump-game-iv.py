 
class Solution:
        
    class Node: 
        def __init__(self, val, dist):
            self.val = val
            self.dist = dist
            self.visited = False
            self.in_q = False

        def __lt__(self, that):
            return self.dist < that.dist

        def __repr__(self):
            return f"<{self.val}: {self.dist}>"
        
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n == 1: 
            return 0
        val_to_ind = {}
        
        val_to_ind = defaultdict(set)
        for i, num in enumerate(arr):
            val_to_ind[num].add(i)

        init_node = self.Node(0, 0)
        queue = [init_node]
        nodes = {0 : init_node}
        queue.append(init_node)
        while len(queue) > 0:
            top = queue.pop(0)
            
            if top.visited:
                continue
                
            index = top.val
            

            poss_arr = val_to_ind[arr[index]]
            val_to_ind.pop(arr[index])
            
            if index + 1 < n:
                poss_arr.add(index+1)
            
            if index -1 >= 0:
                poss_arr.add(index-1)
            
            # print(top, poss_arr)
                
            
            for neighbor_key in poss_arr:
                if neighbor_key == index:
                    continue 
                if neighbor_key == n-1:
                    return top.dist + 1 
                if neighbor_key not in nodes: 
                    nodes[neighbor_key] = self.Node(neighbor_key, math.inf)
                
                neighbor = nodes[neighbor_key]
                if neighbor.visited:
                    continue
                
                new_dist = top.dist +  1
                if new_dist < neighbor.dist:
                    neighbor.dist = new_dist
                    if not neighbor.in_q:
                        queue.append(neighbor)
                        neighbor.in_q = True

            top.visited = True
            
        return nodes[n-1].dist if n-1 in nodes else 0
