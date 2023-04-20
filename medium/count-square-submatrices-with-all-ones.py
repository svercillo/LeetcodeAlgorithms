class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        

        total_count = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    continue

                else:
                    total_count += 1


                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                        total_count += matrix[i][j] -1


        return total_count
