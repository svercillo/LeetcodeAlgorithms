class Solution:
    def numMagicSquaresInside(self, grid) -> int:
        res = 0
        
        n = len(grid)
        m = len(grid[0])

        # print(n)
        # print(m)
        
        
        for i in range(n):
            for j in range(m):
                if i + 2 >= n or j + 2 >= m: 
                    continue
                # print(i, j)

                invalid = False
                
                persis_col_sum = -1
                nums = set([1,2,3,4,5,6,7,8,9])
                for k in range(i, i +3):
                    col_sum = 0 
                    for c in range(j, j+3):
                        t = grid[k][c]
                        if t in nums:
                            nums.remove(t)
                        else: 
                            print("B")
                            invalid = True
                        
                        col_sum += grid[k][c]
                
                    if persis_col_sum == -1: 
                        persis_col_sum = col_sum
                    elif col_sum != persis_col_sum:
                        print("H")
                        invalid = True
                        break


                    
                nums = set([1,2,3,4,5,6,7,8,9])
                persis_row_sum = -1
                for c in range(j, j+3):
                    row_sum = 0 
                    for k in range(i, i+3):
                        t = grid[k][c]
                        if t in nums:
                            nums.remove(t)
                        else: 
                            print("C")
                            invalid = True
                        
                        row_sum += grid[k][c]
                
                    if persis_row_sum == -1: 
                        persis_row_sum = row_sum
                    elif row_sum != persis_row_sum:
                        print("D")
                        invalid = True
                        break

                if invalid: 
                    continue

                diag1 = 0 
                diag2 = 0
                k = i +2
                c = j

                for _ in range(3):

                    diag1 += grid[k][c]

                    k2 = i+ (i +2) - k 

                    print("         ",k, c)
                    print(grid[k2][c], "        ", k2, c)
                    print("         ")
                    diag2 += grid[k2][c]
                    
                    k -=1
                    c +=1
                    
                
                print(nums, i, j, diag1, diag2 )
                if len(nums) == 0 and diag1 == diag2:
                    res +=1

        return res
