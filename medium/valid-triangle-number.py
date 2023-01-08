class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
    
        count = 0
        end = 0
        for i in range(n-2):
            for j in range(i + 1, n):
                _sum = nums[i] + nums[j]

                while end < n and nums[end] < _sum:
                    end += 1
                
                if end > j:
                    count += end - 1 - j 


            end = 0

        return count
