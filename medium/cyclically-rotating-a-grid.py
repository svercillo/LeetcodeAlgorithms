class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n, m = len(grid), len(grid[0])
        nlayers = math.ceil(min(n, m)/ 2)

        # print(nlayers, min(n, m)/ 2)

    
    
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]
        ]


        def shift_array_by_k(arr, k):
            new_arr = []
            for i in range(len(arr)):
                new_arr.append(arr[(k + i) % len(arr)])

            return new_arr




        si, sj = 0, 0
        ei, ej = n-1, m-1
        layers = []
        for _ in range(nlayers):
            layer = []

            i, j = si, sj
            
            for down, right in dirs:

                
                while si <= (i + down) <= ei and sj <= (j + right) <= ej:
                    
                    layer.append(grid[i][j])
                    i += down
                    j += right

            layers.append(layer)
            si += 1
            sj += 1
            ei -= 1
            ej -= 1 

            i += 1
            j += 1


        
        si, sj = 0, 0
        ei, ej = n-1, m-1
        for layer_ind in range(nlayers):
            layer = shift_array_by_k(layers[layer_ind], k)
            
            # print(layer)
            count = 0
            i, j = si, sj
            for down, right in dirs:
                
                
                while si <= (i + down) <= ei and sj <= (j + right) <= ej:
                    grid[i][j] = layer[count]
                    i += down
                    j += right

                    count += 1

            layers.append(layer)
            si += 1
            sj += 1
            ei -= 1
            ej -= 1 

            i += 1
            j += 1


        print( layers)
                
                


        return grid

            
