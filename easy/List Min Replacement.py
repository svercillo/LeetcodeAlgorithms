class Solution:
    def solve(self, nums):
        smallest = []
        small = nums[0]
        
        for i, n in enumerate(nums):

            smallest.append(small)
            if n < small:
                small = n
        

        smallest[0] = 0
        return smallest
