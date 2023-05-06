class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        total = 0

        indr = math.inf
        indr = n
        for indl, e in enumerate(nums):
            # indr = bisect.bisect_left(nums, target - e, lo=indl, hi=indr)
            indr = bisect.bisect_right(nums, target - e)
            
            
            if indr <= indl:
                continue
            # print((nums[indl], nums[indr-1]), (indl, indr))
            

            total += 2 ** (indr -1 - indl) 

            total = total % (10**9 + 7)

        return total
