class Solution:
    def minMoves(self, nums: List[int]) -> int:
        smallest = min(nums)
        nmoves = 0
        for e in nums:
            nmoves += e - smallest

        return nmoves
