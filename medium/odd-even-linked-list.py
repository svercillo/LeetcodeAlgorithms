# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first_even = None
        first_odd = None
        oddtail = ListNode()
        eventail = ListNode()

        node = head

        ind = 0
        while node:
            if ind % 2 == 0:
                if not first_even:
                    first_even = node
                eventail.next = node
                eventail = node
            else:
                if not first_odd:
                    first_odd = node
                oddtail.next = node
                oddtail = node
            
            node = node.next
            ind += 1

        eventail.next = first_odd
        oddtail.next = None
        
        return first_even



