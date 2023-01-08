# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        top = head
        
        
        size = 0
        while top:
            size +=1
            top = top.next
            
        
        

        
        top = head
        steps_to_travel = size -1 -n 
        
        while steps_to_travel:
            try: 
                top = top.next
                steps_to_travel -= 1
            except: 
                return head.next
            
        
        top.next = top.next.next 
        
        
        return head 
