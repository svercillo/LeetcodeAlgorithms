class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()

        sum_arr = []
        _sum = 0
        for e in nums: 
            _sum += e
            sum_arr.append(e)
        
        dp = 0
        result = []

        lp = 0
        for x in range(1, len(nums) + 1):
            solved = False
            

            
            while lp < len(nums) and nums[lp] < x:

                dp |= dp << nums[lp] 
                dp |= 1 << nums[lp] 
                lp += 1

            if dp & 1 << k:

                solved = True

            # print(bin(dp), x, lp)


            copy_lp = lp 
            
            remaining = k
            tp = dp
            while remaining > 0 and copy_lp < len(nums):
                # print(remaining)
                tp |= tp << x 
                tp |= 1 << x

                if tp & 1 << k:
                    solved = True
                    # print ("SDFSDFSDFSDF", x , bin(tp))
                    break
                remaining -= x 
                copy_lp += 1

            result.append(solved)

        return result
