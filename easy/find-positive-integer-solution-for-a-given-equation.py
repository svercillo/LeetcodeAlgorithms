"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        valid = []
        for i in range(1,1001):
            first = True
            skipped = False
            for j in range(1,1001):
                
                print(i, j)
                val = customfunction.f(i, j)

                if val > z:
                    skipped = True
                    break
                elif val == z:
                    valid.append([i,j])
        
            
                first = False
            
            if skipped and first:
                break
        
        return valid
        