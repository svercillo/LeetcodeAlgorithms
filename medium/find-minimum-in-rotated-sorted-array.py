class Solution:
    def findMin(self, nums) -> int:

        if nums[0] <= nums[-1]:  # edge case
            return nums[0]

        arr = nums
        n = len(arr) - 1
        l, r = 0, n - 1

        while l <= r:

            print(arr[l], arr[r])

            m = (l + r) // 2

            if arr[m] < arr[m + 1]:
                l = m + 1

            elif arr[m] > arr[m + 1]:
                r = m - 1

        while l >= 0:
            if l < len(nums) - 1:
                if nums[l] > nums[l + 1]:
                    return nums[l + 1]
            l -= 1
