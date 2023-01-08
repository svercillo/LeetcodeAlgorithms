class LinkedList:
    class Iterator:
        def __init__(self, linkedlist) -> None:
            self.cur = linkedlist.head
            self.linkedlist = linkedlist

        def __iter__(self):
            return self

        def __next__(self):
            if self.cur is None:
                raise StopIteration
            res = self.cur

            self.cur = self.cur.next
            return res

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

    def remove(self, node: Node):
        if self.head is None:
            return -1  # element doesnt exist

        if id(self.head) == id(self.tail):  # pop off first element, len == 1
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

        self.size -= 1

        node.prev = None
        node.next = None

        return node

    def pop_tail(self) -> Node:
        return self.remove(self.tail)

    def pop_head(self) -> Node:
        return self.remove(self.head)

    def is_empty(self) -> bool:
        return self.size == 0

    def __repr__(self) -> str:
        temp = self.head
        s = ""
        while temp is not None:
            s += str(temp)
            temp = temp.next
        return s

    def __str__(self) -> str:
        return self.__repr__()

    def __iter__(self):
        return self.Iterator(self)
    

class MyHashSet:

    def __init__(self):
        self.arr = []
        self.taken_space = 0

    def add(self, key: int) -> None:
        if self.contains(key):
            return 
        
        self.taken_space += 1
        if self.taken_space > len(self.arr) * 0.6:
            self.resize()

        spot = key % len(self.arr)
        
        self.arr[spot].append(key)
            
        
    def resize(self):
        new_array = [LinkedList()] * (self.taken_space * 2  + 177)
        old_arr = self.arr        
        self.arr =  new_array

        for ll in old_arr:
            for e in ll:
                self.add(e.data)
                

    def remove(self, key: int) -> None:
        if len(self.arr) == 0:
            return
        spot = key % len(self.arr)
        
        
        ll = self.arr[spot]
        
        
        for e in ll: 
            if e.data == key:
                to_remove = e
                ll.remove(to_remove)
                
                break
                
    def contains(self, key: int) -> bool:
        if len(self.arr) == 0: 
            return False
        spot = key % len(self.arr)
        ll = self.arr[spot]
        
        for e in ll:
            if e.data == key:
                return True
            
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
