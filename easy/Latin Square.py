class Solution:
    def solve(self, matrix):
        chars = set()

        n = len(matrix)
         



        for i in range(n):
            row = set()
            for j in range(n):
                row.add(matrix[i][j])

                chars.add(matrix[i][j])
            if len(row) < n:
                return False

        if len(chars) != n:
            return False
        
        for j in range(n):
            col = set()
            for i in range(n):
                col.add(matrix[i][j])
            
            if len(col) < n:
                return False

        return True



        
