import math
class Solution:
    def closestMeetingNode(self, edges, node1: int, node2: int) -> int:
        graph = []
        n = len(edges)

        for x, y in enumerate(edges):  
            graph.append(set())
            if y != -1:
                graph[x].add(y)


        def bfs(root, distances):

            q = [root]

            curr_dist = 0

            while len(q) > 0:
                new_q = []
                for node in q:
                    if node in visited:
                        continue
                    visited.add(node)

                    for neigh in graph[node]:
                        new_q.append(neigh)

                    distances[node] = curr_dist
                curr_dist += 1

                q = new_q


        print([(i, graph[i]) for i in range(len(graph))])


        distances1 = [math.inf] * n
        distances2 = [math.inf] * n
        visited = set()
        bfs(node1, distances1)
        visited = set()
        bfs(node2, distances2)

        # print(distances1)
        # print(distances2)


        distances = [0] * n 

        for i in range(n):
            distances[i] = max(distances1[i], distances2[i])


        # print(distances)


        smallest_ind = -1
        for i in range(n):
            if smallest_ind == -1 or distances[i] < distances[smallest_ind]:
                smallest_ind = i

        

        if distances[smallest_ind] < math.inf:
            return smallest_ind
        
        else:
            return -1
