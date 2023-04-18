import math
import heapq


def min_cycle_length(vertices: list, edges: dict):
    class Node:
        def __init__(self, _id):
            self._id = _id
            self.dist = math.inf
            self.explored = False

        def get_name(self):
            return self._id
        
        def is_explored(self):
            return self.explored
        
        def set_explored(self):
            self.explored = True

        def set_dist(self, dist):
            self.dist = dist
        
        def get_dist(self):
            return self.dist

        def __lt__(self, other):
            return self.dist < other.dist

    def create_graph_from_edges(edges : dict):
        graph = {}
        for u, v, l in edges:
            if u not in graph:
                graph[u] = {}

            graph[u][v] = l

        return graph

    # step 1: create constant time access edge graph
    graph = create_graph_from_edges(edges)

    node_map = {}
    for vertex in vertices:
        node_map[vertex] = Node(vertex)

    
    def min_cycle_length_from_starting_node(start_node:Node, visited:set):
        min_cycle_length = math.inf
        if start_node.get_name() in visited:
            return
        
        visited.add(start_node.get_name())
        
        start_node.set_dist(0) # set inital dist to self 0
        priority_queue = [node for node in node_map.values()] # create priority queue from all nodes

        while len(priority_queue):
            top_element:Node = heapq.heappop(priority_queue)
            
            for node_name in graph[top_element.get_name()]:
                neigh:Node = node_map[node_name]
                edge_weight = graph[top_element.get_name()][neigh.get_name()]

                if neigh.is_explored(): # indicates a cycle in graph
                    cycle_length = top_element.get_dist() + edge_weight - neigh.get_dist()

                    min_cycle_length = min(min_cycle_length, cycle_length)
                elif top_element.get_dist() + edge_weight < neigh.get_dist():
                        neigh.set_dist(edge_weight)

                        heapq.heapify(priority_queue) # resort heap if decrease min occurs

            top_element.set_explored()

        return min_cycle_length
    
    visited = set()
    min_cycle_length = math.inf
    for vertex in vertices:
        min_cycle_length = min(
            min_cycle_length, 
            min_cycle_length_from_starting_node(node_map[vertex], visited)
        ) # run dijkstra's on all connected graphs

    return min_cycle_length


    
edges = [
    [0,1,1],
    [1,2,1],
    [2,3,1],
    [3,0,1]
]

vertices = [i for i in range(7)]


res = min_cycle_length(vertices, edges)

from pprint import pprint
pprint(res)

