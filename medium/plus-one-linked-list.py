# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, node: ListNode) -> ListNode:
        
        def addone(node):
            if not node:
                return True
            carry = addone(node.next)
            if carry:
                if node.val == 9:
                    node.val = 0
                    return True
                node.val += 1
            return False

        if addone(node):
            return ListNode(1, node)
        else:
            return node

        


        
        


    
