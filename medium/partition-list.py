# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        size = 0
        node = head 
        while node:
            size += 1
            node = node.next
        head = ListNode(-1, head)
        last = head
        node = head.next
        while size:
            nxt = node.next
            if node.val >= x:
                temp = node
                t_last = last
                
                first_swap = None
                first_swap_par = None
                
                while temp.next:
                    
                    if not first_swap:
                        first_swap = temp.next
                        first_swap_par = t_last
                        
                    # swap 
                    t_last.next = temp.next
                    temp.next = temp.next.next
                    t_last.next.next = temp
                    
                    # iterate
                    t_last = t_last.next
                    
                node = first_swap
                last = first_swap_par
                size -= 1 
                continue
            
            last = node
            node = node.next
            size -=1 
        
        return head.next
