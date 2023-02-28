# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial_arr = []
        
        def dfs(node):
            if not node:
                return 

            serial_arr.append(str(node.val))
            serial_arr.append("L")
            dfs(node.left)
            serial_arr.append("R")
            dfs(node.right)
            # serial_arr.append("-")
            return

        dfs(root)
        serialization = ""
        for c in serial_arr: 
            serialization += c

        return serialization 

        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        prehead = TreeNode(-1)

        is_new_node = True
        val_str = []

        
        # print(data)
        data = data + "L" # so last node is added correctly
    
        print(data)
        stack = [[prehead, "R"]]
        for i in range(len(data)): 
            match data[i]:
                case "L":
                    res = ""
                    for c in val_str:
                        res += c

                    val_str.clear()
                    if res:
                        val = int(res)
                        node = TreeNode(val)
                    else:
                        node = None

                    # print("L: ", stack[-1][0].val, stack[-1][1], val)
                    match stack[-1][1]:
                        case "L":
                            stack[-1][0].left = node
                        case "R": 
                            stack[-1][0].right = node

                    
                    stack.append([node, "L"])
                case "R":
                    print("R: ", stack[-1][0].val, stack[-1][1])

                    while stack[-1][1] == "R":
                        stack.pop()
                    stack[-1][1] = "R"
                case _:                                                                                                                                     
                    val_str.append(data[i])
        
        return prehead.right


        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
