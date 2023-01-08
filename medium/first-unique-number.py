class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data 
            self.prev = None
            self.next = None

        def __str__(self) -> str:
            return f"{self.data}->"

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def append(self, data) -> Node:
        if isinstance(data, self.Node):
            node = data
        else: 
            node = self.Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            node.prev = self.head
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
        self.size += 1
        return node

    def remove(self, node:Node):
        if self.head is None: 
            return -1 # element doesnt exist

        if id(self.head) == id(self.tail): # pop off first element, len == 1
            self.head = None
            self.tail = None
        elif node == self.head:  # pop off first element, len > 1
            self.head = self.head.next 
        elif node == self.tail: 
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
        else: 
            prev_node = node.prev
            next_node = node.next
            
            prev_node.next = next_node
            next_node.prev = prev_node
        
        node.prev = None
        node.next = None
        
        self.size -=1 
        return node
    
    
    def pop_tail(self) -> Node:
        return self.remove(self.tail)
    
    def pop_head(self) -> Node:
        return self.remove(self.head)

    def is_empty(self) -> bool:
        return self.size == 0
    
    def print(self):
        temp = self.head
        s = ""
        while temp is not None:
            s += str(temp)
            temp = temp.next

        print(s)
        return s

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.node_map = {}
        self.q = LinkedList()
        self.invalid = set()
        
        for n in nums:
            self.add(n)
        
        

    
    def showFirstUnique(self) -> int:
        
        if self.q.is_empty():
            return -1
        else:
            # print("SDFDSF")
            # self.q.print()
            # print(self.q.head)
            return self.q.head.data
            
    def add(self, n: int) -> None:
        if n in self.invalid:
            return
        
        if n in self.node_map:
            node = self.node_map[n]
            self.q.remove(node)
            self.node_map.pop(n)
            self.invalid.add(n)
        else:
            # print(self.node_map, n)
            self.q.append(n)
            self.node_map[n] = self.q.tail if self.q.tail else self.q.head


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
