import heapq
import math
class Solution:
    class Node:
        def __init__(self, val, curr_time):
            self.val = val
            self.curr_time = curr_time
            self.duplicate = False

        def __lt__(self, other):
            return self.curr_time < other.curr_time
        

    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:

        graph = {}
        for i in range(n):
                
            if manager[i] == -1:
                continue
            if manager[i] not in graph:
                graph[manager[i]] = []
            graph[manager[i]].append(i)

        node_map = {}
        q = []
        for i in range(n):
            if i == headID:
                continue
            node = self.Node(i, math.inf)
            node_map[i] = node
            q.append(node)

        node_map[headID] = self.Node(headID, 0)
        heapq.heappush(q, node_map[headID])


        print(graph)
        curr_time = 0
        while len(q):
            while len(q) and q[0].duplicate:
                heapq.heappop(q)

            if not len(q): break
            
            top_node = heapq.heappop(q)

            if top_node.val in graph:
                for subord in graph[top_node.val]:

                    next_time = top_node.curr_time + informTime[top_node.val]
                    # print(next_time)

                    if next_time  < node_map[subord].curr_time:
                        updated_node = self.Node(subord, next_time)
                        node_map[subord].duplicate = True
                        node_map[subord] = updated_node
                        heapq.heappush(q, updated_node)

                        if next_time > curr_time:
                            curr_time = next_time       
        return curr_time
    

