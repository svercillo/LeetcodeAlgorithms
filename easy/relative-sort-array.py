class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] +=1
            else:
                freq[n] = 1
        
        return sorted(nums, key=lambda ele: freq[ele] + (1/(ele+2) if ele > 0 else 1 + 1/ (ele-1  *10000)))
