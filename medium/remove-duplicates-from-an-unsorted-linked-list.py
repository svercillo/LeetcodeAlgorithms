# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val}"
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        graph = {}


        prehead = ListNode(0, head)
        node = head 
        while node:
            if node.val not in graph:
                graph[node.val] = 0

            graph[node.val] += 1

            
            node = node.next


        to_delete = []
        node = head
        last = prehead
        while node:
            if node.val in graph and graph[node.val] >= 2:
                to_delete.append(last)
            
            last = node
            node = node.next
        
        for parent in to_delete[::-1]:
            parent.next = parent.next.next

        
        return prehead.next
