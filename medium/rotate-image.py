import math
class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix         
        self.n = len(matrix)
        
        self.swap_rows(0, 0, [])
        
        print(self.matrix)
        
        
    def swap_rows(self, layer:int, _iter:int, copy:List[int]):
        x_start = layer
        x_end = self.n - layer
        
        
        row = [] 
                
        if _iter ==0: # copy left
            for x in range(x_end-1, x_start -1, -1):
                row.append(self.matrix[x][layer])
            
            
                
        elif _iter == 1: # copy top 
            for x in range(x_start, x_end):
                row.append(self.matrix[layer][x])
            
            i =0 
            
            for x in range(x_start, x_end):
                self.matrix[layer][x] = copy[i]
                
                i += 1
                

                
        elif _iter == 2: #copy right 
            
            for x in range(x_end -1, x_start-1, -1):
                row.append(self.matrix[x][self.n -layer-1])
                
            if len(row) ==0:
                return 
            print(row)
            print(copy)
            row[len(row)-1] = copy[len(copy) -1]

            
            i =0 
            for x in range(x_start, x_end):
                self.matrix[x][self.n -layer-1] = copy[i]
                
                i += 1
                 
        elif _iter == 3: # copy bottom
            # print(copy)
            
            
            for x in range(x_start, x_end):
                row.append(self.matrix[self.n -layer-1][x])
            # print(copy)
            
            row[len(row) -1] = copy[0]
            # print(row)
                
#             # put left top
            i =0 
            for x in range(x_start, x_end):
                self.matrix[self.n -layer-1][x] = copy[i]
                    
                i += 1
                
        elif _iter == 4: # copy bottom
            print(copy)

            i=0
            for x in range(x_start, x_end):
                print(self.matrix[x][layer])
                self.matrix[x][layer] = copy[i]
                    
                i += 1
                

        if _iter <4:
            self.swap_rows(layer, _iter+1, row)
        else:
            print(self.matrix )
            if layer < math.floor(self.n/2):
                self.swap_rows(layer+1, 0, row)
        
            
