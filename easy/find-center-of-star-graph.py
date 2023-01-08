class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        undir = {}
        
        
        for x, y in edges:
            if x not in undir:
                undir[x] = set()
                
            if y not in undir:
                undir[y] = set()
                
                

            if len(undir[x]) == 0:
                undir[x].add(y)
            else:
                return x
            if len(undir[y]) == 0: 
                undir[y].add(y)
            else:
                return y
