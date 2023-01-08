class Solution:
    def countHillValley(self, nums) -> int:
        
        n = len(nums)
        count = 0

        i = 1
        while i < n -1:
            t = i
            while t < n-1 and nums[t] == nums[i]:
                t += 1

            if nums[i-1] < nums[i] > nums[t]:
                print(i)
                count += 1
            elif nums[i-1] > nums[i] < nums[t]:
                print(i)
                count += 1
            i = t
        return count
