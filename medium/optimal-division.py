class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        
        # we are trying to maximize the denominator
        # maxDiv(i) == nums[i] / maxDiv(i)

        n = len(nums)
        def buildString(start, end):
            res = []
            for i in range(start, end):
                res.append(str(nums[i]))

                if i != end -1:
                    res.append("/")

            return "".join(res)

        if n <= 2:
            return buildString(0, n)
        
        return str(nums[0]) + "/(" + buildString(1, n) + ")"
