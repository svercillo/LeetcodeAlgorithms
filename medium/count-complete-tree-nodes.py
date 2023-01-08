
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        depth = self.depth(root)
        print(depth)
        if depth == 0:
            return 1
        elif depth == -1:
            return 0
        
        res = self.binary_search(depth, root)
        return res
                
    def binary_search(self, depth, root):
        
        def check_leaf(node, bin_code):
            
            print("bin_code", bin_code)
            
            i = 0
            while i < depth and node:            
                c = bin_code[i]
                
                if c == "0":
                    node = node.left
                else: 
                    node = node.right
                i +=1

            return i == depth and node is not None
                

        ind = 2 ** depth
        curr = 0 
        
        last_res = True
        while ind >= 1:
            binary = bin(ind // 2  + curr)[2:]
            binary = "0" * (depth - len(binary)) + binary
            
            last_res = check_leaf(root, binary)
            
            if last_res:
                curr += ind // 2
            ind //= 2
            
            
        print(curr)
        return curr  + 2 ** (depth)
                            
    def depth(self, root):    
        if root == None: return -1 
        return self.depth(root.left) +1
        
