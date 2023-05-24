class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        _min, _max = math.inf, -math.inf
        _min_ind = -1
        _max_ind = -1

        for i, e in enumerate(nums):
            if e < _min:
                _min = e
                _min_ind = i

            if e > _max:
                _max = e
                _max_ind = i

        ind1, ind2 = sorted([_max_ind, _min_ind])
        n = len(nums)


        return min(ind2 + 1, (ind1 + 1) + (n - ind2), n - ind1)



