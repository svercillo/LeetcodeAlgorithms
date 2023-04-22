class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        instances = defaultdict(lambda : [])
        for i, e in enumerate(nums):
            instances[e].append(i)

        res = [0] * n
        for value in instances:
            inds_arr = instances[value]

            prefix = 0
            presum = []

            for ind in inds_arr:
                prefix += ind
                presum.append(prefix)
            
            ind_size = len(inds_arr)
            for i, ind in enumerate(inds_arr):
                num_st = i # num inds smaller than ind
                num_gt = ind_size - 1 - i # num inds greater than ind

                ind_total = 0 

                if i > 0:
                    ind_total += ind * num_st - presum[i-1]
                
                if i < ind_size - 1:
                    ind_total += (presum[ind_size -1] - presum[i]) - ind * num_gt


                res[ind] = ind_total

            
        return res


