class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # good pair, j -i == nums[j] - nums[i]4
        n = len(nums)
        freq = defaultdict(lambda : 0)
        count = 0
        for j, e in enumerate(nums):
            b = e - j
            count += freq[b]
            freq[b] += 1

        return n * (n-1) // 2 - count
