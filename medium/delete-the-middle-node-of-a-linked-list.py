# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        size = 0
        node = head
        while node:
            node = node.next
            size += 1

        if size <= 1:
            return None

        mid_ind = size // 2 
        
        node = head
        pre_mid = None
        mid = None
        index = 0
        while index < size:

            if index == mid_ind -1:
                pre_mid = node
            elif index == mid_ind:
                mid = node
            index += 1
            node = node.next

        pre_mid.next = mid.next

        return head
