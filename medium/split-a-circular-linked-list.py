# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, head: Optional[ListNode]) -> List[Optional[ListNode]]:
        if not head:
            return []

        size = 1
        node = head
        while True:
            size += 1

            node = node.next
            if node.next == head:
                break

        first_size = math.ceil(size / 2)
        first_size -= 1 # include head node

        print(first_size)

        first_head = head
        node = head 
        while first_size:
            print("SDFSDF")
            node = node.next
            first_size -=1 


        second_head = node.next
        node.next = first_head

        node = second_head
        while node.next != first_head:
            node = node.next


        node.next = second_head


        return [first_head, second_head]
