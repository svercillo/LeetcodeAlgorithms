"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
            
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        if id(head) == id(head.next):
            newnode = Node(insertVal, head.next)
            head.next = newnode
            return head
        
        node = head
        
        smallest_node = node
        smallest = node.val
        smallind = 0
        largest = node.val
        largestind = 0
        largest_node = node
        
        count = 1
        node = node.next
        
        while id(node) != id(head):
            if node.val < smallest:
                smallest = node.val
                smallind = count
                smallest_node = node
            
            elif node.val >= largest:
                largest = node.val
                largestind = count
                largest_node = node
                
            node = node.next
            count += 1
                  
        if largest == smallest: # monotonic array
            newnode = Node(insertVal, head.next)
            head.next = newnode
            return head
            
            
        if insertVal >= largest or insertVal <= smallest:
            newnode = Node(insertVal, largest_node.next)
            largest_node.next = newnode
        else:
            node = smallest_node
            
            prev = node
            while node.val < insertVal:
                prev = node
                node = node.next
            
            newnode = Node(insertVal, node)
            prev.next = newnode
            
            
            
        return head

  
