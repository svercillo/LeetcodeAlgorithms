class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n =  len(mat)
    
        total = 0
        for i in range(n):
            total += mat[i][i]
            total += mat[n-1 -i][i]
            if i == n -1 -i:
                total -= mat[i][i]

        return total
