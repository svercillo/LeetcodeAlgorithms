class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        dp = [0]* (10 ** 4  + 1) 
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dp[mat[i][j]] += 1

        for e, freq in enumerate(dp):
            if freq == len(mat):
                return e

        return -1
                
