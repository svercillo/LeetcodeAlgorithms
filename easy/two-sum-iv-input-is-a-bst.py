# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        in_order = []
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            in_order.append(node.val)
            dfs(node.right)
            
        dfs(root)
        
        if len(in_order) <= 1:
            return False
        
        
        return self.twoSum(in_order, k)
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        
        freq = {}
        for i in range(len(numbers)):
            e = numbers[i]
            if e not in freq:
                freq[e] = [i]
                
            else: 
                freq[e].append(i)
        i =0
        while i < n:
            e = numbers[i]
            if e > target // 2 +1:
                break
            diff = target - e
            if diff in freq:
                if diff == e:
                    return len(freq[diff]) >= 2
                else:
                    print(e, diff)
                    return True
            i += 1
        
        return False
