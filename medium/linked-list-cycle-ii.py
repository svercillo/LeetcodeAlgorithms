class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        visited = {}

        node = head
        index = 0
        while node:
            if id(node) in visited:
                return visited[id(node)]
            visited[id(node)] = node

            index += 1
            node = node.next

        return None
