"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node = head
        dup_mapping = {} # mem address of node to mem address of duplicate node
        
        while node is not None:
            dup_mapping[id(node)] = Node(node.val)
            node = node.next

        node = head
        while node is not None:
            
            duplicate = dup_mapping[id(node)]


            if node.next is not None:
                duplicate.next = dup_mapping[id(node.next)]

            if node.random is not None:
                duplicate.random = dup_mapping[id(node.random)]

            node = node.next
        
        

        return dup_mapping[id(head)]
