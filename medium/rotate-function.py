class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        def calc(offset): 
            total = 0
            for i in range(n):

                ind = (i + offset) % n
                total += i * nums[ind]

            return total
        s = sum(nums)

        running = calc(0)
        # print(running)
        mval = running
        for i in range(n-1): 
            running = running - s +  n  * nums[i]

            # print(i, running)

            mval = max(mval, running)

        return mval

