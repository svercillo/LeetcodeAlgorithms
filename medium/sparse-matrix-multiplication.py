class Solution:
    def multiply(self, mat1, mat2):

        m = len(mat1)
        k = len(mat2)
        n = len(mat2[0])

        res = []
        for i in range(m):
            row = []

            for i in range(n):
                row.append(0)

            res.append(row)

        for i in range(m):
            for j in range(n):

                dot_product = 0
                for p in range(k):
                    dot_product += mat1[i][p] * mat2[p][j]

                res[i][j] = dot_product

        return res
