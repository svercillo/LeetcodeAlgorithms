# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start_node = ListNode(-1, head)
        
        if not head: 
            return head
        elif not head.next:
            return head
        
        old_head = start_node 
        
        
        def swap(node):
            if node.next is None: 
                return node
            
            temp = node
            sec = node.next
            temp.next = sec.next
            sec.next = temp
            
            return sec
            

        while old_head is not None:
            swapped = swap(head)
            print(swapped, swapped.next)
            
            old_head.next = swapped
            old_head = swapped.next
            
            if old_head and old_head.next:
                head = old_head.next
            else:
                break
            
            
        return start_node.next
        
            
