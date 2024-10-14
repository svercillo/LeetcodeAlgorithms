class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):

            allOnes = True
            for j in range(n):
                if j == i:
                    continue
                
                if grid[i][j] != 1:
                    allOnes = False
                    break


            if allOnes:
                return i
        return -1

