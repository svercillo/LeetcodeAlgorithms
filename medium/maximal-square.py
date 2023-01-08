from pprint import pprint
class Solution:
    def maximalSquare(self, matrix) -> int:
        
        n, m = len(matrix), len(matrix[0])

        largest = 0
        for i in range(n):
            for j in range(m):


                matrix[i][j]  = int(matrix[i][j])

                if matrix[i][j] == 0:
                    continue
                
                temp_top = 0 if i ==0 else matrix[i-1][j]
                temp_left = 0 if j ==0 else matrix[i][j-1]
                temp_diag = 0 if i == 0 else matrix[i-1][j-1]
                

                if temp_diag > 0  and temp_top > 0 and temp_left > 0:
                    matrix[i][j] = min([temp_diag,temp_top, temp_left]) + 1

                largest = max(largest, matrix[i][j])
        

        return largest ** 2
