class MaxStack:
    class Node:
        def __init__(self, val, ind):
            self.val = val
            self.invalid = False
            self.ind = ind


        def __lt__(self, other):

            if self.val == other.val:
                return self.ind > other.ind
            
            return self.val > other.val

        def __repr__(self):
            return f"Node<{self.val}, {self.invalid}>"

    def __init__(self):
        self.stack = []
        self.heap = []

        self.insertion_index = 0

    def push(self, x: int) -> None:
        
        new_node = self.Node(x, self.insertion_index)
        self.insertion_index += 1

        while len(self.stack) and self.stack[-1].invalid:
            self.stack.pop()
        self.stack.append(new_node)

        while len(self.heap) and self.heap[0].invalid:
            heapq.heappop(self.heap)
            
        heapq.heappush(self.heap, new_node)
        
        #print("push", self.stack)


    def pop(self) -> int:
        while len(self.stack) and self.stack[-1].invalid:
            self.stack.pop()

        top = self.stack.pop()
        top.invalid = True

        while len(self.stack) and self.stack[-1].invalid:
            self.stack.pop()

        return top.val

    def top(self) -> int:
        return self.stack[-1].val
        

    def peekMax(self) -> int:

        #print(self.heap)
        while len(self.heap) and self.heap[0].invalid:
            heapq.heappop(self.heap)

        top = heapq.heappop(self.heap)
        heapq.heappush(self.heap, top)
        #print("peek", top)
        return top.val
        
    def popMax(self) -> int:

        while len(self.heap) and self.heap[0].invalid:
            heapq.heappop(self.heap)

        top = heapq.heappop(self.heap)
        top.invalid = True

        while len(self.stack) and self.stack[-1].invalid:
            self.stack.pop()
        return top.val
