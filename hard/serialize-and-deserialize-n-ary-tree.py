"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:    

    class Node(object):
        def __init__(self, val=None):
            self.val = val
            self.children = []

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        serial_arr = []
        
        def dfs(node):
            if not node:
                return 

            serial_arr.append(str(node.val))            
            serial_arr.append("L")
            num_children = len(node.children)
            for i in range(num_children):
                dfs(node.children[i])
            serial_arr.append("R")
            return

        dfs(root)
        serialization = ""
        for c in serial_arr: 
            serialization += c

        return serialization 

        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        class Node(object):
            def __init__(self, val=None, children=[]):
                self.val = val
                self.children = children

        prehead = self.Node(-1)

        is_new_node = True
        val_str = []

        data = data # so last node is added correctly
        stack = [prehead]
        for i in range(len(data)): 
            if data[i] == "L":
                res = ""
                for c in val_str:
                    res += c
                val_str.clear()
                if res:
                    val = int(res)
                    node = self.Node(val)


                # print(f"ADDING NODE {node.val} TO NODE'S {stack[-1].val} CHILDREN", id(stack[-1].children))
                # print([n.val for n in stack if n], stack[-1].val, node.val)
                stack[-1].children.append(node)
                stack.append(node)

            elif data[i] == "R":
                stack.pop()
            else:
                val_str.append(data[i])
        if not len(prehead.children):
            return None
        
        return prehead.children[0]
