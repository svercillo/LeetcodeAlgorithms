# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        node = head 

        while node.next:
            if node.next.val < 0:
                nxt = node.next
                after_nxt = nxt.next
                
                nxt.next = head
                head = nxt

                node.next = after_nxt

            else: 
                node = node.next
        


        return head
