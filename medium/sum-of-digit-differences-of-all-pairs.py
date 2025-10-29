class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        # for each index: map of num to freq 
        l = len(str(nums[0]))

        n = len(nums)
        freq_maps = []

        for _ in range(l):
            freq_maps.append([0 for _ in range(10)])
    
        for num in nums:
            str_num = str(num)
            for i in range(l):
                freq_maps[i][int(str_num[i])] += 1

        total = 0
        for num in nums:
            str_num = str(num)
            for i in range(l):
                dig = int(str_num[i])
                total += n - freq_maps[i][dig]

        return total //  2 
