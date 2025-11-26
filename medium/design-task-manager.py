from pprint import pprint
from heapq import heappush, heappop

class Node:
    def __init__(self, p, uid, tid):
        self.p = p
        self.uid = uid
        self.tid = tid
        self.invalid = False

    def __lt__(self, other):
        if self.p == other.p:
            return self.tid > other.tid
        return self.p > other.p

    def __repr__(self):
        return f"Task<{self.uid} ,{self.tid}, {self.p} , {self.invalid}"

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.nmap = {}
        q = []
        for uid, tid, p in tasks:
            node = Node(p, uid, tid)
            heappush(q, node)
            self.nmap[tid] = node
        self.q = q


    def add(self, uid, tid, p) -> None:
        node = Node(p, uid, tid)
        self.nmap[tid] =node
        heappush(self.q, node)
        
    def edit(self, tid: int, p: int) -> None:
        node = self.nmap[tid]
        node.invalid = True

        nnode = Node(p, node.uid, tid)
        heappush(self.q, nnode)
        self.nmap[tid] = nnode

    def rmv(self, tid: int) -> None:
        node = self.nmap[tid]
        node.invalid = True
        # # # # print("removing")
        # # # # print(node)
        self.nmap.pop(tid)
        
        
    def execTop(self) -> int:
        # # # print(self.q)
        while len(self.q) and self.q[0].invalid:
            node = heappop(self.q)

        if not len(self.q ):
            return -1
        
        node  = heappop(self.q)

        self.nmap.pop(node.tid)
        return node.uid
                
        

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
