class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        graph = defaultdict(lambda : set())
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        odd_degree_nodes = []
        for node in graph:
            if len(graph[node]) % 2 == 1:
                odd_degree_nodes.append(node)

        match len(odd_degree_nodes):
            case 0: 
                return True
            case 1:
                return False
            case 2:
                first, second = odd_degree_nodes
                
                if second in graph[first]:
                    # if first and second can be connected to a third even node
                    for third in range(1, n):
                        if third in [first, second]: continue

                        if first not in graph[third] and second not in graph[third]:
                            print(third)
                            return True
                else:
                    return True
                
        
            case 4:
                first, second, third, fourth = odd_degree_nodes
                if (
                    (first not in graph[second] and third not in graph[fourth])
                    or (first not in graph[third] and second not in graph[fourth])
                    or (first not in graph[fourth] and second not in graph[third])
                ):
                    return True

                return False
            case _:
                return False
