"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, root: 'Optional[Node]') -> 'Optional[Node]':

        head = Node(0, None, None, None)
        curr = head

        def dfs(node):
            nonlocal curr
            if not node:
                return

            # print(node.val, curr.val)
            right_branch = node.next
            curr.next = node
            node.prev = curr
            curr = node

            dfs(node.child)
            # curr = node
            node.child = None
            dfs(right_branch)



        dfs(root)

        temp = head.next
        while temp:
            temp.prev = None
            break



        return temp
