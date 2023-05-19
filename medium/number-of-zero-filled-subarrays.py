class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0
        total = 0
        while i < n:


            if nums[i] == 0:
                start = i
                while i < n and nums[i] == 0:
                    end = i
                    i += 1


                size = end - start + 1

                total += size * (size + 1) // 2


                print(size)

            i += 1

        return total
