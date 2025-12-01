class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        

        if preorder[0] == "#":
            if len(preorder) == 1:
                return True
            return False
        
        sarr = preorder.split(",")
        stack = [(sarr[0], 0)]
        for e in sarr[1:]:
            # print(e, stack)

            if not len(stack):
                return False
            tope, topc = stack.pop()

            if topc == 0:
                stack.append((tope, topc +1))


            if e != "#":
                stack.append((e, 0))


        return not len(stack)

                


