# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        stack = []

        head = node


        while node:
            while len(stack) > 0 and node.val > stack[-1].val:
                top = stack.pop() 
                top.val = node.val
            
            
            stack.append(node)

            node = node.next

        while len(stack) != 0:
            top = stack.pop()
            top.val = 0

        
        
        return head

                
