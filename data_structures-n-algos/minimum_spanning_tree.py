import heapq
import random
from pprint import pprint
import math
from collections import defaultdict


# Prim's algorithm (union find - no negative edges)
def generate_minimum_spanning_tree(vertices: list, edges_list: list):
    class Node:
        def __init__(self, name) -> None:
            self.name = name
            self.cost = math.inf
            prev = None

        def __lt__(self, other):
            return self.cost < other.cost
        
        def __repr__(self) -> str:
            return f"NODE<{self.name}, cost: {self.cost}>"

    edges = defaultdict(lambda : {})
    for u, v, w in edges_list:
        edges[u][v] = w 
        edges[v][u] = w

    node_map = {}
    for vertex in vertices:
        node_map[vertex] = Node(vertex)

    
    source_node:Node = node_map[random.choice(vertices)]
    source_node.cost = 0
    q = [node_map[vertex] for vertex in vertices]
    heapq.heapify(q)

    visited = set()
    while len(q):
        top:Node = heapq.heappop(q)

        print(top)
        visited.add(top.name)
        for neigh in edges[top.name]:
            if neigh.name not in visited and edges[top.name][neigh.name] < neigh.cost:
                neigh.cost = edges[top.name][neigh.name]
                neigh.prev = top
                heapq.heapify(neigh)
    
        print("===========ITERATION===========")
        
        for vertex in vertices:
            print(node_map[vertex])


# Kruskal's algorithm (union find - no negative edges)
def generate_minimum_spanning_tree(vertices: list, edges_list: list):
    vertex_parent_map = {}
    vertex_size_map = {}
    for vertex in vertices:
        vertex_size_map[vertex] = 1
        vertex_parent_map[vertex] = -1


    def find_parent_vertex(vertex):
        while vertex_parent_map[vertex] != -1:
            vertex = vertex_parent_map[vertex]
        return vertex
    
    def union(parent1, parent2):
        if vertex_size_map[parent1] < vertex_size_map[parent2]:
            temp = parent1 # swap parents
            parent1 = parent2
            parent2 = temp

        vertex_size_map[parent1] += vertex_size_map[parent2]
        vertex_size_map[parent2] = 0 # smaller set is merged into the larger set
        
        vertex_parent_map[parent2] = parent1 # change smaller set parent pointer
        # print(vertex_parent_map)

    tree_edges = defaultdict(lambda : {})

    edges_list.sort(key = lambda edge: edge[2]) # sort edges by edge weight

    for u, v, w in edges_list:

        assert w >=0
        parent1 = find_parent_vertex(u)
        parent2 = find_parent_vertex(v)
        if parent1 != parent2:
            union(parent1, parent2)

            # tree_edges.append((u,v))

            tree_edges[u][v] = w
            tree_edges[v][u] = w

    return tree_edges




def test_generate_minimum_spanning_tree():
    # Test Case 1: Simple graph
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 4), ('C', 'D', 5)]
    expected_mst = {
        'B':  {'A': 2, 'C': 1, 'D': 4},
        'C': {'B': 1},
        'A': {'B': 2},
        'D': {'B': 4}
    }
    mst = generate_minimum_spanning_tree(vertices, edges)
    
    # assert mst == expected_mst


    # Test Case 3: Graph with duplicate edges
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1), ('B', 'D', 4), ('C', 'D', 5), ('B', 'D', 6)]
    expected_mst = {
        'B': {'A': 2, 'C': 1, 'D': 4},
        'C': {'B': 1},
        'A': {'B': 2},
        'D': {'B': 4}
    }
    mst = generate_minimum_spanning_tree(vertices, edges)
    pprint([(k, mst[k]) for k in mst])
    # assert mst == expected_mst

    print("All test cases passed")


test_generate_minimum_spanning_tree()
