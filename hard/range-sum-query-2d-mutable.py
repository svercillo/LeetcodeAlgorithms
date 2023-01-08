
def binary_search(array, target):
    if len(array) == 0:
        return None, False

    n = len(array)
    l, r = 0, n - 1

    while l <= r:
        m = (l + r) // 2

        if array[m][0] == target:
            return m, True
        elif array[m][0] > target:
            r = m - 1
        else:
            l = m + 1

    if l == n:
        return n, False
    while array[l][0] > target and l >= 0:
        l -= 1

    return l +1, False

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
        self.matrix = matrix
        self.updates = [[] for _ in range(self.n)]
        
    def update(self, row: int, col: int, val: int) -> None:
        
        urow = self.updates[row]
        
        ind, found = binary_search(urow, col)
        
        diff = val - self.matrix[row][col]
        if found:
            urow[ind] = (col, diff) # override
        else:
            if ind == None:
                ind = 0
            urow.insert(ind, (col, diff))
            
        x = 3
            
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        total = 0   
        for i in range(r1, r2 +1):
            urow = self.updates[i]
            
            ind1, _ = binary_search(urow, c1)
            ind2, found2 = binary_search(urow, c2)
            
            if ind1 is None and ind2 is None:
                continue
            if ind1 is None:
                ind1 = 0
            if ind2 is None:
                ind2 = self.n

            if found2:
                ind2 += 1
            for j in range(ind1, ind2):
                total += urow[j][1]
        
        
        if (r1, c1) == (r2, c2):
            return self.matrix[r1][c1] + total
        
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
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
