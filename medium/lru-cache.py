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
        
        return node
    
    
    def pop_tail(self) -> Node:
        return self.remove(self.tail)
    
    def pop_head(self) -> Node:
        return self.remove(self.head)

    
    def print(self):
        temp = self.head
        s = "" 
        while temp is not None: 
            s += str(temp)
            temp = temp.next
        
        print(s)
        return s

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.ll = LinkedList()
        
        

    def get(self, key: int) -> int:
        
        if key not in self.cache: 
            return -1
        
        node = self.cache[key]
        self.ll.remove(node)

        self.ll.append(node) # replace MRU
        return node.data[1] # data[1] is value 

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.data[1] = value
            self.ll.remove(node)

            self.ll.append(node) # replace MRU

        else:
            if len(self.cache) + 1 > self.capacity:
                lru = self.ll.pop_head() # pop LRU
                self.cache.pop(lru.data[0]) # [0] is key [1] is value
            
            new_node = LinkedList.Node(data=[key, value])
            self.ll.append(new_node)
            self.cache[key] = new_node
            
