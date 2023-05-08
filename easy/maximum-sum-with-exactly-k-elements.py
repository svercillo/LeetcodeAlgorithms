class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        largest = max(nums)

        return (largest + k) * (largest + k -1 ) // 2 - largest * (largest -1) // 2
