class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        # sliding window
        rp = 0
        _min = nums[0]
        _max = nums[0]
        n = len(nums)

        partitions = 1
        while rp < n:
            
            _min = min(_min, nums[rp])
            _max = max(_max, nums[rp])

            if _max - _min > k:
                partitions += 1
                _min = nums[rp]
                _max = nums[rp]

            rp += 1


        return partitions
