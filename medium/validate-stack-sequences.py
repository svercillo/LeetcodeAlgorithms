class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # pointer 1 and pointer 2 
        p1 = 0 
        p2 = 0
        
        if len(pushed) != len(popped):
            return False
        
        n = len(pushed)
        stack = []
        while p1 < n : 
            
            if pushed[p1] != popped[p2]: # push
                stack.append(pushed[p1])
                p1 += 1
                
            else:
                p1 += 1
                p2 += 1
                
                while p2 < n and len(stack) > 0 and stack[len(stack) -1] == popped[p2]:
                    stack.pop()
                    p2 +=1 
                    

        
        print(p1, p2, stack)
        while p2 < n:
            
            res = stack.pop() 

            if res != popped[p2]:
                return False
            p2 += 1
        
        return True
                
