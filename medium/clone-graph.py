"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, first_node: 'Node') -> 'Node':
        if not first_node: 
            return None 
        root = Node(first_node.val) 
        
        queue = [(first_node, root)] 
        
        m = set({})
        
        hashmap = {root.val: root}
        
        
        while len(queue) > 0: 
            node, copy_node = queue.pop(0)
            
            
            if node.val in m:
                continue
                
            print(node.val, copy_node.val)
            
            
            m.add(node.val)
            
            for n in node.neighbors:
                
                if n.val not in hashmap:
                    new_copy = Node(n.val)
                    hashmap[n.val] = new_copy
                else: 
                    new_copy = hashmap[n.val]
                
                queue.append((n, new_copy))
                print("         ", n.val, new_copy.val)
                copy_node.neighbors.append(new_copy)
            
        return root
            
