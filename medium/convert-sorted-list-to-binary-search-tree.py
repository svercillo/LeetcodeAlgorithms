Select tags
0/5
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        length = 0
        node = head

        arr = []
        
        while node:
            arr.append(node.val)
            node = node.next
            
        def create_bst(lp, rp):
            if rp - lp == 1:
                new_r_node = TreeNode(arr[rp])
                return TreeNode(arr[lp], None, new_r_node)
            elif rp - lp == 0: 
                return TreeNode(arr[lp])

            if not (0 <= lp < len(arr)) or not (0 <= rp < len(arr)):
                return None

            

            m = (lp + rp) // 2
            new_node = TreeNode(arr[m])
            new_node.left = create_bst(lp, m -1)

            new_node.right = create_bst(m+1, rp)

            return new_node

        return create_bst(0, len(arr)-1)
