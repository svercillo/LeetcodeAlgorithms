# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descs: List[List[int]]) -> Optional[TreeNode]:
        graph = defaultdict(lambda : [-1,-1])
        has_parent = set()

        for parent, child, isleft in descs:
            graph[parent][0 if isleft else 1] = child
            has_parent.add(child)


        node_map = {}
        for parent in graph:
            # left = TreeNode(graph[parent][0]) if graph[parent][0] != -1 else None
            # right = TreeNode(graph[parent][1]) if graph[parent][1] != -1 else None
            left = graph[parent][0]
            right = graph[parent][1]

            if left == -1: 
                left_node = None
            else:
                if left not in node_map:
                    left_node = TreeNode(left)
                else:
                    left_node = node_map[left]

            if right == -1:
                right_node = None
            else:
                if right not in node_map:
                    right_node = TreeNode(right)
                else:
                    right_node = node_map[right]

            if parent in node_map:
                parent_node = node_map[parent]
            else:
                parent_node = TreeNode(parent)
            
            parent_node.left = left_node
            parent_node.right = right_node

            node_map[left] = left_node
            node_map[right] = right_node
            node_map[parent] = parent_node

        
        for parent in graph:
            if parent not in has_parent:
                return node_map[parent]


        return None
