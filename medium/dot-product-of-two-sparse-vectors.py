class SparseVector:
    def __init__(self, nums: List[int]):
        
        self.values = self.convertArr(nums)
        
            
        
    def convertArr(self, arr):
        values = []
        for i, n in enumerate(arr):
            if n != 0:
                values.append([i, n])
                
                
        return values
                
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        vecValues = vec.values
        
        p1, p2 = 0, 0
        
        n = len(self.values)
        m = len(vecValues)
        
        
        _sum = 0
        while p1 < n and p2 < m:
            # print(p1, p2, self.values, vecValues)
            if self.values[p1][0] == vecValues[p2][0]:
                _sum += self.values[p1][1] * vecValues[p2][1]
                p1 +=1
                p2 += 1
            elif self.values[p1][0] < vecValues[p2][0]:
                p1 +=1
            else:
                p2 +=1
                
        return _sum
                
        


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
