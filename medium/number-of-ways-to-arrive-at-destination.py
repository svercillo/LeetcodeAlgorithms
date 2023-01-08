import math
import heapq


class Solution:
    class Node:
        def __init__(self, val, dist):
            self.val = val
            self.dist = dist
            self.visited = False
            self.num_ways = 0
            self.in_q = False

        def __lt__(self, that):
            return self.dist < that.dist  # we want a reversed heap

        def __repr__(self):
            return f"<{self.val}: {self.dist}, {self.num_ways}>"

    def countPaths(self, n: int, roads) -> int:
        if len(roads) == 0:
            return 1
        start = 0
        end = n - 1

        conns = {}
        for i in range(len(roads)):
            e = roads[i]
            p = e[2]

            if e[0] not in conns:
                conns[e[0]] = {e[1]: p}
            else:
                conns[e[0]][e[1]] = p

            if e[1] not in conns:
                conns[e[1]] = {e[0]: p}
            else:
                conns[e[1]][e[0]] = p

        if start not in conns:
            return 0  # no paths out
        nodes = {n: self.Node(n, math.inf) for n in conns}

        nodes[start].dist = 0
        nodes[start].num_ways = 1

        queue = [nodes[start]]

        while len(queue) > 0:
            # print("queue", queue)
            top = heapq.heappop(queue)
            # print("Top ", top.val)
            if top.visited:
                continue

            index = top.val
            for neighbor_key in conns[index]:

                neighbor = nodes[neighbor_key]
                if neighbor.visited:
                    continue

                new_dist = top.dist + conns[top.val][neighbor.val]
                if new_dist < neighbor.dist:
                    neighbor.dist = new_dist
                    # print("---", neighbor.val, queue)
                    if not neighbor.in_q:
                        neighbor.num_ways = top.num_ways
                        neighbor.in_q = True
                        heapq.heappush(queue, neighbor)
                    else:
                        heapq.heapify(queue)

                elif new_dist == neighbor.dist:
                    neighbor.num_ways += top.num_ways
            top.visited = True

        return nodes[end].num_ways % ((10 ** 9) + 7) if end in nodes else 1
