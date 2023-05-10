class LinkedList:

    class Node:
        def __init__(self, count):
            self.count = count
            self.key_set = set()
            self.prev = None
            self.next = None
        
        def __str__(self):
            return f"Node(count: {self.count}, key_set: {self.key_set})"

        def __repr__(self):
            return f"Node<{self.count}>"

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node_after(self, before_node, count, initial_key):
        new_node = self.Node(count)
        new_node.key_set.add(initial_key)
        
        if not before_node and not self.head: # first node 
            self.head = new_node
            self.tail = new_node
        elif not before_node and self.head: 
            nxt_node = self.head
            nxt_node.prev = new_node
            new_node.next = self.head

            self.head = new_node
                
        elif before_node == self.tail:
            prev_node = self.tail
            
            prev_node.next = new_node
            new_node.prev = prev_node

            self.tail = new_node

        else: # general case
            nxt_node = before_node.next

            before_node.next = new_node
            nxt_node.prev = new_node

            new_node.prev = before_node
            new_node.next = nxt_node

        return new_node
    
    def remove_node(self, node):
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            nxt_node = self.head.next
            nxt_node.prev = None

            self.head = nxt_node

        elif node == self.tail:
            prev_node = self.tail.prev 
            prev_node.next = None

            self.tail = prev_node

        else: # general case
            prev_node = node.prev
            nxt_node = node.next

            prev_node.next = nxt_node
            nxt_node.prev = prev_node

    def __repr__(self):
        res = "LINKED LIST: \n"
        node = self.head
        while node is not None:
            res += str(node)
            res += " -> "
            node = node.next


        # res += "\n\nREV LINKED LIST: \n"
        # node = self.tail
        # while node is not None:
        #     res += str(node)
        #     res += " -> "
        #     node = node.prev

        return res

class AllOne:

    def __init__(self):
        self.freq_map = {}
        self.ll = LinkedList()

    def inc(self, key: str) -> None:        
        if not self.ll.head:
            count = 1
            new_node = self.ll.insert_node_after(None, count, key)
            self.freq_map[key] = new_node
        elif key not in self.freq_map:
            count = 1
            if self.ll.head.count == 1:
                self.ll.head.key_set.add(key)

                self.freq_map[key] = self.ll.head
            else:
                new_node = self.ll.insert_node_after(None, count, key)

                self.freq_map[key] = new_node   
        else:
            assert key in self.freq_map

            prev_node = self.freq_map[key]
            prev_node.key_set.remove(key)
            count = prev_node.count + 1
            
            nxt_node = prev_node.next
            if not nxt_node or nxt_node.count != count:
                incr_node = self.ll.insert_node_after(prev_node, count, key)
            else:
                incr_node = nxt_node
                incr_node.key_set.add(key)

            if len(prev_node.key_set) == 0:
               self.ll.remove_node(prev_node)
            
            self.freq_map[key] = incr_node

        # print()
        # print()
        # print()
        # print("incr", key, self.ll)


    def dec(self, key: str) -> None:
        assert key in self.freq_map

        node = self.freq_map[key]
        node.key_set.remove(key)

        prev_node = node.prev
        if len(node.key_set) == 0:
            self.ll.remove_node(node)

        decr_count = node.count - 1

        if decr_count == 0:
            self.freq_map.pop(key)
            return
        elif not prev_node:
            new_node = self.ll.insert_node_after(None, decr_count, key)
            self.freq_map[key] = new_node
        elif prev_node.count == decr_count:
            prev_node.key_set.add(key)
            self.freq_map[key] = prev_node
        else:
            new_node = self.ll.insert_node_after(prev_node, decr_count, key)

            self.freq_map[key] = new_node

        # print()
        # print()
        # print()
        # print("decr", key, self.ll)




    def getMaxKey(self) -> str:
        if not self.ll.head:
            return ""

        tail = self.ll.tail
        
        random_key = tail.key_set.pop()
        tail.key_set.add(random_key) 

        return random_key
        

    def getMinKey(self) -> str:
        if not self.ll.head:
            return ""

        head = self.ll.head
        
        random_key = head.key_set.pop()
        head.key_set.add(random_key) 

        return random_key
        
