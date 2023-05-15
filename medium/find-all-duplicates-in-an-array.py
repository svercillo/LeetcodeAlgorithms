LARGE =  10**6

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:



        n = len(nums)

        for i in range(n):
            e = abs(nums[i])

            if e > LARGE:
                e -= LARGE

            print(i,e)

            if nums[e - 1] < 0:
                nums[e -1] -= LARGE
            else: 
                nums[e-1] *= -1


        print(nums)
        res = []
        for i, e in enumerate(nums):
            if e < - LARGE:
                res.append(i +1)



        return res
