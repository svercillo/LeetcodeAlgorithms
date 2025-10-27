from pprint import pprint

class Solution:
    def candyCrush(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        def convert():
            for i in range(n):
                for j in range(m): 

                    if grid[i][j] == 1:
                        grid[i][j] = 2001 
                    elif grid[i][j] == 2001: 
                        grid[i][j] = 1
    
        def normalizegrid(): 
            for i in range(n):
                for j in range(m): 
                    grid[i][j] = norm(grid[i][j])

        

        def norm(c):
            if c == 0: 
                return 0
            c = abs(c)
            if c < 1:
                c = c ** -1
            return c
            
        def markboard():
            print('marking')
            changed = False
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0:
                        continue
                    
                    went_right = 0 < grid[i][j] < 1
                    went_down = grid[i][j] < 0
                    if (
                        not went_right and
                        j +2 < m and 
                        norm(grid[i][j]) == norm(grid[i][j+1]) == norm(grid[i][j+2])
                    ):
                        changed = True
                        tj = j
                        while tj < m and norm(grid[i][tj]) == norm(grid[i][j]):
                            grid[i][tj] = norm(grid[i][tj]) ** -1
                            tj += 1

                    if (
                        not went_down and
                        i +2 < n and 
                        norm(grid[i][j]) == norm(grid[i+1][j]) == norm(grid[i+2][j])
                    ):
                        changed = True
                        ti = i
                        while ti < n and norm(grid[ti][j]) == norm(grid[i][j]):
                            grid[ti][j] = norm(grid[ti][j]) * -1
                            ti += 1
            return changed

        def collapse():
            print('collapsing')
            for j in range(0, m):
                count_to_skip = 0

                first_non_zero = math.inf
                for i in range(n-1, -1, -1):
                    if grid[i][j] == 0:
                        continue

                    first_non_zero = i
                    went_right = 0 < grid[i][j] < 1
                    went_down = grid[i][j] < 0

                    if went_right or went_down:
                        count_to_skip +=1
                    else:
                        grid[i + count_to_skip][j] = grid[i][j]
                        # print(grid[i][j], grid[i + count_to_skip][j], ( i,j), count_to_skip)
                for offset in range(count_to_skip):
                    grid[first_non_zero + offset][j] = 0

        convert() # change 1 to 2001s
        has_change = markboard()
        # pprint(grid)
        while has_change:
            collapse()
            # pprint(grid)

            has_change = markboard()
            # pprint(grid)

            collapse()
            # pprint(grid)

            has_change = markboard()
            # pprint(grid)
            

            # break
            
        convert()
        normalizegrid()        
                 
        return grid
                    




                

                
                

        
