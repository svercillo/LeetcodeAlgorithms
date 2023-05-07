# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        print(root)
        self.added_children = set()
    
    def next(self) -> int:
        stack = self.stack
        print([s.val for s in stack])
        

        top = stack.pop()
        while id(top) not in self.added_children:
            if top.right:
                stack.append(top.right)
            
            stack.append(top)
            if top.left:
                stack.append(top.left)

            self.added_children.add(id(top))
            top = self.stack.pop()

        return top.val
            


                    
    def hasNext(self) -> bool:
        return len(self.stack) > 0
        
