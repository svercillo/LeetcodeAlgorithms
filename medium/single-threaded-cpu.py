from collections import deque
import heapq
class Solution:
    class Node:
        def __init__(self, enque_time, processing_time, index):
            self.enque_time = enque_time
            self.processing_time = processing_time
            self.index = index

        def __lt__(self, other):
            if self.processing_time == other.processing_time: 
                return self.index < other.index

            return self.processing_time < other.processing_time

        def __repr__(self):
            return f"Node<{self.enque_time}, {self.processing_time}, {self.index}>"
                
    def getOrder(self, tasks: List[List[int]]) -> List[int]:


        task_inds = zip(tasks, [i for i in range(len(tasks))])
        task_inds = sorted(task_inds, key = lambda k : k[0][0])



        print(task_inds)
        
        time = tasks[0][0]

        task_inds = deque(task_inds)
        q = []

        order = []
        ind = 0
        sim_time = 0
        while len(task_inds):
            if len(q):
                top = heapq.heappop(q)
                order.append(top.index)
                sim_time += top.processing_time
            
            while len(task_inds) and task_inds[0][0][0] <= sim_time:
                top = task_inds.popleft()
                heapq.heappush(q, self.Node(top[0][0], top[0][1], top[1]))

            if len(q) == 0 and len(task_inds) > 0 and sim_time < task_inds[0][0][0]:
                sim_time = task_inds[0][0][0]

        while len(q):
            top = heapq.heappop(q)
            order.append(top.index)
            sim_time += top.processing_time

        return order
