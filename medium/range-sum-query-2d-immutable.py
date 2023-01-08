from pprint import pprint
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        
        totals = []
        prefix = []
        suffix = []
        for i in range(self.n):
            presum = 0
            prow = [0] * self.m
            suffsum = 0
            srow = [0] * self.m
            for j in range(self.m):
                
                presum += matrix[i][j]
                prow[j] = presum
                
                
                suffsum += matrix[i][self.m - 1 - j]
                srow[self.m - 1 -j] = suffsum
                
            totals.append(prow[-1])
            prefix.append(prow)
            suffix.append(srow)
        
        self.totals = totals
        self.prefix = prefix
        self.suffix = suffix
        
        # pprint(self.prefix)
        # pprint(self.suffix)
        
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        
        if (r1, c1) == (r2, c2):
            return self.matrix[r1][c1]
        
        total = 0
        for i in range(r1, r2 + 1):
            if c1 == 0:
                pre = 0
            else:
                pre = self.prefix[i][c1 - 1]

            if c2 == self.m -1:
                suff = 0
            else:
                suff = self.suffix[i][c2 + 1]
        
            total += self.totals[i] - pre - suff
            
        return total
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
