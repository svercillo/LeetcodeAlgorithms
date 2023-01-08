class Solution:
    def wiggleMaxLength(self, nums) -> int:

        if len(nums) < 2:
            return len(nums)
        elif len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2

        difference = 0
        n = len(nums)
        for i in range(n - 1):
            nums[i] = nums[i + 1] - nums[i]
            difference += abs(nums[i + 1] - nums[i])

        if difference == 0:
            return 1

        i = n - 2
        while i >= 0:
            if nums[i] == 0:
                nums.pop(i)
            i -= 1
        nums.pop()
        i = 0
        while i < len(nums) - 1:
            nums[i] = nums[i] * nums[i + 1]
            i += 1
        nums.pop()


        count = 0
        for n in nums:
            if n < 0:
                count += 1

        return count + 2
