class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        n = len(mat)
        m = len(mat[0])

        mapping = [0] * (len(arr) + 1)

        for i in range(n):
            for j in range(m):
                mapping[mat[i][j]] = (i, j)
            
        col_count = [0] * m
        row_count = [0] * n
        

        for index, val in enumerate(arr):
            i, j = mapping[val]

            row_count[i] += 1
            col_count[j] += 1

            if row_count[i] == m:
                return index
            if col_count[j] == n:
                return index

        return -1
