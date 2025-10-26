class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def cansplitwithmax(maxvalue, k):
            running = 0
            narrays = 1
            for e in nums:
                if e > maxvalue:
                    return False

                if e + running > maxvalue:
                    narrays += 1

                    if narrays > k:
                        return  False
                    running = 0
                running += e
            return True


        l,r = min(nums), max(nums) *  n
        while l < r:
            m = (l + r) //2

            if cansplitwithmax(m, k):
                r = m
            else:
                l = m + 1


        maxvalue = l

        return maxvalue
