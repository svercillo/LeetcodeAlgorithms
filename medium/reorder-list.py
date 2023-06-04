# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        length = 0

        node = head

        while node:
            node = node.next
            length += 1


        # find middle node
        node = head
        for i in range(math.ceil(length/ 2)):
            node = node.next

        mid = node


        prev = None
        while node:            
            nxt_node = node.next
            node.next = prev
            prev = node
            node = nxt_node

        new_mid = prev
        while node:
            node = node.next

        node = new_mid
        while node:
            print(node.val)
            node = node.next


        node = head
        while node.next != mid:
            node = node.next
        node.next = None


        last_r = None

        l, r = head, new_mid 
        while r:
            lnxt = l.next
            rnxt = r.next

            if last_r:
                last_r.next = l
            last_r = r
            l.next = r
            
            l = lnxt
            r = rnxt


        if last_r:
            last_r.next = l
