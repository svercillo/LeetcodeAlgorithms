class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        def visitValue(value):
            if value not in visited:
                new_q.append(value)
                visited.add(value)
                
            
        visited = set()
        
        q = [x] 
        num_operations = 0
        while len(q):
            print(q)
            new_q = []
            for x in q:
                if x == y: 
                    return num_operations
                
                visitValue(x-1)
                visitValue(x+1)
                if x % 5 == 0:
                    visitValue(x //5)
                if x % 11 == 0:
                    visitValue(x // 11)


            q = new_q
            num_operations += 1
            
            
        return -1
