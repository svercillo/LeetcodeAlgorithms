class Solution:
    def canReach(self, arr, start: int) -> bool:
        n = len(arr)
        if arr[start] == 0: return True
        
        queue = [start] 
        while len(queue) > 0: 

            top = queue.pop()

            if not (0 <=  top <=  n -1):
                continue
                
            val = arr[top]
            i = val
            if (0 <=  top + i<=  n -1) and arr[top +i] != -1:
                if arr[top+i] == 0:
                    return True 
                if val - i > arr[top +i]:
                    arr[top+i] = -1 # we can go to any path here
                else:
                    queue.append(top +i)
            
            if (0 <=  top - i<=  n -1) and arr[top -i] != -1: 
                if arr[top-i] ==0:
                    return True

                if val -i > arr[top-i]:
                    arr[top-i] = -1
                else: 
                    queue.append(top - i)
                        
            arr[top] = -1 # signify visited
        
        return False
