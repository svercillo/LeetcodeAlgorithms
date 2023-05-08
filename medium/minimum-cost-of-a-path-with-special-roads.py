class Solution:

    def generate_graph(self, start, target, special):
        # idea: generate a graph with the cost from all possible edges, then run dijkstra's
        def calc_diff(coords1, coords2):
            return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])

        graph = defaultdict(lambda : defaultdict(lambda : math.inf))
        for i in range(len(special)):
            x1, y1, x2, y2, cost = special[i]
            graph[(x1, y1)][(x2, y2)] = min(
                cost,
                calc_diff(
                    (x1, y1),
                    (x2, y2)
                ),
                graph[(x1, y1)][(x2, y2)]
            )

            cost_start_to = calc_diff(
                tuple(start),
                (x1, y1)
            )
            graph[tuple(start)][(x1, y1)] = min(
                cost_start_to,
                graph[tuple(start)][(x1, y1)]
            )

            cost_to_targ = calc_diff(
                (x2, y2),
                tuple(target)                
            )
            graph[(x2, y2)][tuple(target)] = min(
                cost_to_targ,
                graph[(x2, y2)][tuple(target)]
            )
            
        for i in range(len(special)):
            for j in range(len(special)):
                if i == j: 
                    continue

                _, _, first_x2, first_y2, _ = special[i]
                second_x1, second_y1, _, _, _ = special[j]

                cost = calc_diff(
                    (first_x2, first_y2),
                    (second_x1, second_y1)
                )
                
                graph[(first_x2, first_y2)][(second_x1, second_y1)] = min(
                    cost,
                    graph[(first_x2, first_y2)][(second_x1, second_y1)]
                )


        cost_start_to_end = calc_diff(start, target)
        graph[tuple(start)][tuple(target)] = min(
            cost_start_to_end,
            graph[tuple(start)][tuple(target)]
        )
        # from pprint import pprint
        # pprint([(k,graph[k]) for k in graph])

        return graph

    def minimumCost(self, start: List[int], target: List[int], special: List[List[int]]) -> int:

        class Node:
            def __init__(self, coords):
                self.coords = coords
                self.dist = math.inf
                self.invalid = False

            def __lt__(self, other):
                return self.dist < other.dist

        graph = self.generate_graph(start, target, special)

        node_map = {node: Node(node) for node in graph}
        node_map[tuple(target)] = Node(tuple(target))

        q = [node_map[node] for node in graph]
        node_map[tuple(start)].dist = 0

        heapq.heapify(q)
        while len(q):
            top_node = heapq.heappop(q)
            top = top_node.coords 

            # print(top)
            if top == tuple(target):
                return top_node.dist

            if top_node.invalid:
                continue
            
            # visited.add(top_node.coords)

            for neigh in graph[top]:
                neigh_node = node_map[neigh]

                if top_node.dist + graph[top][neigh] < neigh_node.dist:
                    neigh_node.invalid = True
                
                    new_neigh_node = Node(neigh_node.coords)
                    new_neigh_node.dist = top_node.dist + graph[top][neigh]

                    node_map[neigh] = new_neigh_node
                    heapq.heappush(q, new_neigh_node)
                

        return math.inf
