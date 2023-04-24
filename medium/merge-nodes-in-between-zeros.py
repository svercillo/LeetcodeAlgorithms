# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        combination_head = ListNode()
        combination_tail = combination_head

        node = head
        combination_node = None
        while node:
            combination_node = ListNode()
            while node and node.val != 0:
                combination_node.val += node.val
                node = node.next
            
            
            combination_tail.next = combination_node
            combination_tail = combination_node

            node = node.next
        


        return combination_head.next.next
