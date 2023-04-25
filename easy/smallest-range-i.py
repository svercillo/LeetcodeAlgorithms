class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0

        largest = max(nums)
        smallest = min(nums)


        if largest - smallest <= 2 *k:
            return 0

        else:
            return largest- smallest - 2 * k
