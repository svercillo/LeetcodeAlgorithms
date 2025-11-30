class Node:
    def __init__(self, arr, p):
        self.arr = arr
        self.p = p

        self.prev = None
        self.nxt = None

class LinkedList:
    def __init__(self, arrays):        
        self.count = 0

        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.nxt = self.tail
        self.tail.prev = self.head

        for arr in arrays: 
            self.append(Node(arr, 0 ))

    def append(self, node:Node):
        before = self.tail.prev 

        before.nxt = node
        node.prev = before

        node.nxt = self.tail
        self.tail.prev = node

        self.count += 1

    def remove(self, node:Node):
        before = node.prev 
        after = node.nxt

        before.nxt = after
        after.prev = before

        node.nxt = None
        node.prev = None
        self.count -=1
    
    def size(self):
        return self.count
 
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        arrays = [v for v in [v1, v2 ]  if len(v)]
        self.linkedlist = LinkedList(arrays)
        self.node = self.linkedlist.head.nxt 
        self.forward = True

    def next(self) -> int:
        # print("getting next")
        node = self.node
        res = node.arr[node.p] 
        node.p += 1
    
        nxt = node.nxt
        prev = node.prev

        shouldswaparrs = self.linkedlist.size() > 1

        if node.p == len(node.arr):
            self.linkedlist.remove(node)

        if shouldswaparrs:
            if self.forward:
                if nxt == self.linkedlist.tail:
                    self.node = prev
                    self.forward ^= True
                else: 
                    self.node = nxt
            else:
                if prev == self.linkedlist.head:
                    self.node = nxt
                    self.forward ^= True
                else: 
                    self.node = prev
        return res
        

    def hasNext(self) -> bool:
        return self.linkedlist.size() > 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
