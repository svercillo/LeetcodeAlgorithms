# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        new_tail = head
        
        
        node = head.next
        print(node)
        while node:
            next_node = node.next
            
            if node.val <= new_head.val: 
                if id(new_head) == id(new_tail):
                    new_head = node
                    new_head.next = new_tail
                else: 
                    node.next = new_head
                    new_head = node
                    
                new_tail.next = next_node
            
            elif node.val > new_tail.val:
                
                if id(new_head) == id(new_tail):
                    
                    new_tail = node
                    new_head.next = new_tail
                    

                else:
                    
                    new_tail.next = node
                    new_tail = node
            else:
                
                new_tail.next = next_node
                ordered = new_head
                
                prev = None
                while node.val > ordered.val:
                    prev = ordered
                    ordered = ordered.next
                    
                prev.next = node
                node.next = ordered
        
            node = next_node
            
        return new_head
