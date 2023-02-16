class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        ind_to_num = {}
        num_to_ind = {}
        for i, e in enumerate(nums):
            ind_to_num[i] = e
            num_to_ind[e] = i

        for first, second in operations:
            ind = num_to_ind[first]
            ind_to_num[ind] = second

            num_to_ind.pop(first)
            num_to_ind[second] = ind

        

        for ind in ind_to_num:
            nums[ind] = ind_to_num[ind]


        return nums


        
