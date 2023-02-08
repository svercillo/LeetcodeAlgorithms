class Solution:
    def distinctIntegers(self, n: int) -> int:
        
        
        
        q = [n] 
        
        visited = set()
        while len(q):
            newq = []            
            for node in q:
                if node in visited:
                    continue
                visited.add(node)
                for second in range(1, node): 
                    if node % second == 1:
                        newq.append(second)
                        
            
            q = newq
            
        return len(visited)
            
            
