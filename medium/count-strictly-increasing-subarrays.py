class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        count = 0
        greatest = -1
        subarr_start = -1
        for i,e in enumerate(nums):
            if greatest == -1:
                greatest = e
                subarr_start = i
            else:
                if e > greatest:
                    print(e, i - subarr_start)
                    count += i - subarr_start
                    greatest = e
                else:
                    greatest = e
                    subarr_start = i


            count += 1

        return count
            