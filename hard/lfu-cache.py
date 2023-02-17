class LFUCache:
    class Node:
        def __init__(self, key, val, freq, last_used):
            self.key = key
            self.val = val
            self.freq = freq
            self.last_used = last_used
            self.invalid = False
        
        def __lt__(self, other):
            if self.freq == other.freq:
                return self.last_used < other.last_used
            return self.freq < other.freq


        def __repr__(self):
            res = ""

            return f"Node<{self.key}, {self.val} "


    def __init__(self, capacity: int):
        self.node_map = {}
        self.lfu = []
        self.capacity = capacity
        self.ind = 0

    def get(self, key: int) -> int:
        self.ind += 1
        
        if key not in self.node_map:
            return -1

        node = self.node_map[key]
        node.invalid = True
        new_node = self.Node(key,  node.val, node.freq +1, self.ind)
        self.node_map[key] = new_node

        heapq.heappush(self.lfu, new_node) # push new node to avoid heapify
        return node.val
        
    def put(self, key: int, value: int) -> None:
        self.ind += 1
        
        if key in self.node_map: # update already existing node
            node = self.node_map[key]
            node.invalid = True

            new_node = self.Node(key, value, node.freq +1, self.ind)
            self.node_map[key] = new_node
            heapq.heappush(self.lfu, new_node) # push new node to avoid heapify
        else: # add new node

            if len(self.node_map) == self.capacity: # if capacity is full and we're inserting new Node
                # pop off any invalidated nodes
                while len(self.lfu)  > 0 and self.lfu[0].invalid:
                    heapq.heappop(self.lfu)

                # pop off one not-yet invalidated node
                if len(self.lfu) > 0: 
                    top_node = heapq.heappop(self.lfu)
                    
                    self.node_map.pop(top_node.key) # remove from node map
                            
            # insert new node
            new_node = self.Node(key, value, 0, self.ind)
            heapq.heappush(self.lfu, new_node)
            self.node_map[key] = new_node
