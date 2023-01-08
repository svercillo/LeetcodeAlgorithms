class Solution:
    def subsets(self, nums):
        
        results = [[]]

        n = len(nums)


        def remaining(input, start):
            nonlocal n
            
            results.append(input)

            for i in range(start +1, n):
                new = input.copy()
                new.append(nums[i])
                remaining(new, i)

        for i in range(n):

            remaining([nums[i]], i)
            

        
        return results
