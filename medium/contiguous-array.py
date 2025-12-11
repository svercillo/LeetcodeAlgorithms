class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        prefix = {}
        nones = 0
        nz = 0
        largest = 0        
        for i, e  in enumerate(nums):
            if e == 0:
                nones += 1
            else:
                nz += 1
            diff = nones - nz

        
            if diff in prefix:
                largest = max(largest, i - prefix[diff])
            else:
                prefix[diff] = i

            if diff ==0: 
                largest = max(i +1, largest)

        return largest


    

