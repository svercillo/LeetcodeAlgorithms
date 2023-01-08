class Solution:
    def largestMagicSquare(self, grid) -> int:
        
        
        n = len(grid)
        m = len(grid[0])


        res = 1

        for i in range(n):
            for j in range(m):

                for h in range(res, min(m, n)):
                    
                    if i + h >= n or j + h >= m: 
                        continue


                    invalid = False
                    
                    persis_col_sum = -1
                    for k in range(i, i +h+1):
                        col_sum = 0 
                        for c in range(j, j+h+1):
                            col_sum += grid[k][c]
                    
                        if persis_col_sum == -1: 
                            persis_col_sum = col_sum
                        elif col_sum != persis_col_sum:
                            invalid = True
                            break

                    persis_row_sum = -1
                    for c in range(j, j+h+1):
                        row_sum = 0 
                        for k in range(i, i+h+1):
                            row_sum += grid[k][c]
                    
                        if persis_row_sum == -1: 
                            persis_row_sum = row_sum
                        elif row_sum != persis_row_sum:
                            invalid = True
                            break


                    if invalid: 
                        continue

                    diag1 = 0 
                    diag2 = 0
                    k = i +h
                    c = j

                    for _ in range(h+1):

                        diag1 += grid[k][c]

                        k2 = i+ (i +h) - k 
                        diag2 += grid[k2][c]
                        
                        k -=1
                        c +=1
                        
                    # print(diag1, diag2)
                    if diag1 == diag2 == persis_col_sum == persis_row_sum:
                        res = max(h+1, res)

        return res
