
import heapq
import math
class Solution:
    class Node: 
        def __init__(self, letter, dist):
            self.letter = letter
            self.dist = dist
            self.invalid = False

        def __lt__(self, other): 
            return self.dist < other.dist
        
        def __repr__(self):
            return f"Node<{self.letter}, {self.dist}>"


    def minimumCost(self, source, target, original, changed, cost) -> int:    
        
        nsource = len(source)
        ntarget = len(target)

        if nsource != ntarget:
            return -1


        # print(original)
        # print(changed)
    
        nodes = set()
        swap_cost = {}
        for i in range(len(original)):
            if changed[i] not in swap_cost:
                swap_cost[changed[i]] = {}

            nodes.add(changed[i])
            nodes.add(original[i])

            if (
                original[i] not in swap_cost[changed[i]] 
                or cost[i] < swap_cost[changed[i]][original[i]]
            ):
                swap_cost[changed[i]][original[i]] = cost[i]

        for c in source:
            nodes.add(c)
        
        for c in target:
            nodes.add(c)
        # print(swap_cost)


        self.nodes = nodes
        self.cost_map = swap_cost

        total_sum = 0
        # for i in [4]:
        for i in range(nsource):
            cost = self.find_cheapest_path(target[i], source[i])
            # print(f"\nCost of {target[i]} -> {source[i]}: (ind {i}, cost {cost}")

            if cost == -1: 
                return -1

            total_sum += cost
        return total_sum 

    
    @cache
    def find_cheapest_path(self, start, end):

        cost_map = self.cost_map
        nodes = self.nodes
        # print(f"Find cheapest {start}, {end}\n\n\n")
        if start == end: 
            return 0
        
        node_map = {n : self.Node(n, math.inf) for n in nodes}
        node_map[start].dist = 0

        q = [node_map[n] for n in nodes]
        
        # heapify the q after initializing starting node to 0
        heapq.heapify(q)
        while len(q):
            # print(q)
            while len(q) and q[0].invalid:
                heapq.heappop(q) # pop off unused nodes

            if not len(q):
                continue 

            top = heapq.heappop(q)

            if top.letter == end: 
                return top.dist if top.dist != math.inf else -1 
        
            if top.letter not in cost_map: 
                continue
            
            for neigh_n in cost_map[top.letter]:
                neigh = node_map[neigh_n]

                cost_to_travel = cost_map[top.letter][neigh_n]
            
                if cost_to_travel + top.dist < neigh.dist: 
                    new_dist = cost_to_travel + top.dist

                    neigh.invalid = True
                    new_node = self.Node(neigh_n, new_dist)
                    node_map[neigh_n] = new_node
                    
                    heapq.heappush(q, new_node)
                    
            # print(q)

        return -1
