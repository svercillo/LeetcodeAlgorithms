class Solution:
    def longestOnes(self, nums, k: int) -> int:
        start = 0
        end = 0
        n = len(nums)

        m1s = 0
        flipped = 0
        ones = 0

        while end < n:
            if end - start > m1s:
                m1s = end - start
            if nums[end] == 0:
                if k - flipped > 0:
                    flipped += 1
                    end += 1
                else:
                    if nums[start] == 1:
                        while nums[start] == 1:
                            start += 1

                    start += 1
                    end += 1
            else:
                end += 1

        if end - start > m1s:
            m1s = end - start

        return m1s
