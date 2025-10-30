class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        

        @cache
        def maxJForI(ind):
            mvalue = nums[ind] + maxDiff

            insertion_ind = bisect_left(nums, mvalue + 1)

            if insertion_ind -1 == ind: 
                return ind

            return maxJForI(insertion_ind -1)

        res = []
        for a, b in queries:

            a, b = sorted([a, b])


            largest= maxJForI(a)

            res.append(largest >= b)

        return res
